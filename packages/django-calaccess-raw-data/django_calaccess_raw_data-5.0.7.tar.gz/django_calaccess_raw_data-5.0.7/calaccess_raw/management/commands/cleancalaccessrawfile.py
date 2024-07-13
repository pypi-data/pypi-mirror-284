"""
Clean a source CAL-ACCESS TSV file and reformat it as a CSV.
"""
import os
import csv

import csvkit
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    """
    Clean a source CAL-ACCESS TSV file and reformat it as a CSV.
    """

    help = "Clean a source CAL-ACCESS TSV file and reformat it as a CSV"

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "file_name",
            help="Name of the TSV file to be cleaned and discarded for a CSV",
        )
        parser.add_argument(
            "--keep-file",
            action="store_true",
            dest="keep_file",
            default=False,
            help="Keep original TSV file",
        )

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        # Set all the config options
        self.set_options(options)

        # If the file has data ...
        if self.row_count:
            # Walk through the raw TSV file and create a clean CSV file
            if self.verbosity > 1:
                self.log(" Cleaning %s" % self.file_name)
            self.clean()

        # Unless keeping files, remove the raw TSV file
        if not options["keep_file"]:
            os.remove(self.tsv_path)

    def set_options(self, options):
        """
        Set options for use in other methods.
        """
        # Set options
        self.file_name = options["file_name"]

        # Set log variables
        self.log_dir = os.path.join(self.data_dir, "log/")
        self.log_name = self.file_name.lower().replace("tsv", "errors.csv")
        self.error_log_path = os.path.join(self.log_dir, self.log_name)
        self.log_rows = []

        # Make sure the log directory exists
        os.path.exists(self.log_dir) or os.makedirs(self.log_dir)

        # Input and output paths
        self.tsv_path = os.path.join(self.tsv_dir, self.file_name)
        self.csv_name = self.file_name.lower().replace("tsv", "csv")
        self.csv_path = os.path.join(self.csv_dir, self.csv_name)

        # Pull and clean the headers
        self.headers = self.get_headers()
        self.headers_count = len(self.headers)

        # Get the row count
        with open(self.tsv_path, "r") as tsv_file:
            self.row_count = max(sum(1 for line in tsv_file), 0)

    def get_headers(self):
        """
        Returns the headers from the TSV file.
        """
        with open(self.tsv_path, "r") as tsv_file:
            tsv_reader = csvkit.reader(tsv_file, delimiter=str("\t"))
            try:
                return next(tsv_reader)
            except StopIteration:
                return []

    def _convert_tsv(self):
        """
        Given it a raw list of rows from a TSV, yields cleaned rows for a CSV.
        """
        with open(self.tsv_path, "rb") as tsv_file:
            # Pop the headers out of the TSV file
            next(tsv_file)

            # Loop through all the rows
            for tsv_line in tsv_file:
                # Decode the line for testing
                tsv_line = tsv_line.decode("ascii", "replace")

                # If the line is empty skip it
                if not tsv_line.strip():
                    continue

                # Nuke any null bytes
                if tsv_line.count("\x00"):
                    tsv_line = tsv_line.replace("\x00", " ")

                # Nuke the ASCII "substitute character." chr(26) in Python
                if tsv_line.count("\x1a"):
                    tsv_line = tsv_line.replace("\x1a", "")

                # Remove any extra newline chars
                tsv_line = (
                    tsv_line.replace("\r\n", "").replace("\r", "").replace("\n", "")
                )

                # Split on tabs so we can later spit it back out as a CSV row
                csv_line = tsv_line.split("\t")
                csv_field_count = len(csv_line)

                # If it matches the header count, yield it
                if csv_field_count == self.headers_count:
                    yield csv_line
                else:
                    # Otherwise log it
                    self.log_rows.append(
                        [self.headers_count, csv_field_count, ",".join(csv_line)]
                    )

    def clean(self):
        """
        Cleans the provided source TSV file and writes it out in CSV format.
        """
        # Create the output object
        with open(self.csv_path, "w") as csv_file:
            # Create the CSV writer
            csv_writer = csvkit.writer(csv_file)
            # Write the headers
            csv_writer.writerow(self.headers)
            # Write out the rows
            [csv_writer.writerow(row) for row in self._convert_tsv()]

        # Log errors if there are any
        if self.log_rows:
            # Log to the terminal
            if self.verbosity > 2:
                msg = "  {} errors logged (not including empty lines)"
                self.failure(msg.format(len(self.log_rows)))

            # Log to the file
            with open(self.error_log_path, "w") as log_file:
                log_writer = csvkit.writer(log_file, quoting=csv.QUOTE_ALL)
                log_writer.writerow(["headers", "fields", "value"])
                log_writer.writerows(self.log_rows)
