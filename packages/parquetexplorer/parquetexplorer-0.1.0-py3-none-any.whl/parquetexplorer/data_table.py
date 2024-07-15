import os
from itertools import cycle
from pathlib import Path  # Add this import to handle file paths

import fire
import polars as pl
from fit2parquets import fit2parquets
from rich.text import Text
from textual.app import App, ComposeResult
from textual.widgets import DataTable, DirectoryTree

from parquetexplorer.utils.logger import logger


class TableApp(App):
    CSS_PATH = "grid.tcss"

    def __init__(self, fit_file_folder: str):
        super().__init__()
        self.cursors = cycle(["row", "column", "cell"])
        self.folder = fit_file_folder
        self.df = pl.read_parquet(
            os.path.join(self.folder, "record_mesgs.parquet")
        )

    def compose(self) -> ComposeResult:
        """Create the table."""
        yield DirectoryTree(
            self.folder,
            id="static1",
        )
        yield DataTable(id="static2")

    def on_mount(self) -> None:
        """Add the data to the table."""
        self.update_table()

    def update_table(self):
        """Update the DataTable with new DataFrame."""
        table = self.query_one(DataTable)
        table.clear(columns=True)  # Clear existing data
        table.cursor_type = next(self.cursors)  # type: ignore
        table.zebra_stripes = True
        table.add_columns(*self.df.columns)
        for number, row in enumerate(self.df.iter_rows()):
            label = Text(str(number), style="#B0FC38 italic")
            table.add_row(*row, label=label)
        table.fixed_columns = 1

    def on_directory_tree_file_selected(self, file_selected):
        """Handle file selection from DirectoryTree."""
        file_path = file_selected.path
        logger.debug(f"File selected: {file_path}")
        selected_file = Path(file_path)
        if selected_file.suffix == ".parquet":
            try:
                self.df = pl.read_parquet(selected_file)
                self.update_table()
            except Exception as e:
                logger.error(f"Error reading {selected_file}: {e}")
        else:
            logger.warning(
                f"Selected file {selected_file} is not a .parquet file."
            )

    def key_c(self):
        """Toggle cursor type."""
        table = self.query_one(DataTable)
        table.cursor_type = next(self.cursors)  # type: ignore


def explore(fit_file: str) -> None:
    fit_file_folder = fit_file.replace(".fit", "")
    if not os.path.exists(fit_file_folder):
        fit2parquets(fit_file)
    app = TableApp(fit_file_folder)
    app.run()


if __name__ == "__main__":
    fire.Fire(explore)
