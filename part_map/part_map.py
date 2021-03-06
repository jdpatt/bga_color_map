"""Main Window of Part Map"""
from pathlib import Path

from PySide2 import QtWidgets

from .gui import Ui_MainWindow
from .logger import ThreadLogHandler, setup_logger
from .object import PartObject


class PartMap(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main Part Map Window."""

    def __init__(self, filename=None, settings=None):
        QtWidgets.QMainWindow.__init__(self)
        self.log = setup_logger("partmap")

        self.part = None
        self.view = None

        screen_resolution = QtWidgets.QApplication.instance().screens()[0].size()
        if not settings:
            settings = {
                "refdes": "",
                "rotate": True,
                "circles": False,
                "labels": True,
            }
        settings.update(
            {
                "width": screen_resolution.width(),
                "height": screen_resolution.height(),
                "margin": 5,
            }
        )
        self.settings = settings

        self.setupUi(self)
        self.properties.setVisible(False)
        self.menubar.setNativeMenuBar(False)
        self.connect_actions()

        thread_log = ThreadLogHandler()
        self.log.addHandler(thread_log)
        thread_log.new_record.connect(self.log_message)
        if filename:
            self.load_file(Path(filename))

    def connect_actions(self):
        """Connect any actions to slots."""
        # pylint: disable=W0201
        self.actionOpen.triggered.connect(self.prompt_user_for_file)
        self.actionSave_as_Image.triggered.connect(self.save_image)
        self.actionSave_as_Json.triggered.connect(self.save_json)
        self.actionRotate.triggered.connect(self.rotate)
        self.actionToggle_Shape.triggered.connect(self.change_shape)
        self.actionToggle_Labels.triggered.connect(self.toggle_labels)
        self.actionZoom_In.triggered.connect(self.zoom_in)
        self.actionZoom_Out.triggered.connect(self.zoom_out)
        self.actionDecrease_Font_Size.triggered.connect(self.decrease_font)
        self.actionIncrease_Font_Size.triggered.connect(self.increase_font)
        self.actionReset_Zoom.triggered.connect(self.reset_zoom)

    def log_message(self, level, msg) -> None:
        """Log any logger messages via the slot/signal mechanism so that its thread safe."""
        del level  # Unused
        self.statusbar.showMessage(msg, timeout=5000)  # Miliseconds

    def prompt_user_for_file(self):
        """Load a file into the gui."""
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            self.tr("Load Project"),
            "",
            self.tr("Part Map File (*.json *.net *.txt *.xlsx *.xlsm *.xltm)"),
        )
        if filename:
            self.load_file(Path(filename))

    def load_file(self, filename: Path):
        """Read in a file and create a part."""
        self.setWindowTitle(filename.stem)
        self.log.info(f"Filename: {filename}")
        if filename.suffix in [".xlsx", ".xlsm", ".xltm"]:
            self.part = PartObject.from_excel(filename)
        elif filename.suffix in [".json"]:
            self.part = PartObject.from_json(filename)
        elif filename.suffix in [".net", ".txt"]:
            self.part = PartObject.from_telesis(filename, self.settings["refdes"])

        self.settings.update({"filename": filename})
        self.view.setup(self.part, self.settings)

    def save_image(self):
        """Save the view as an image."""
        if self.view:
            self.view.save()
        else:
            self.log.error("View doesn't exist")

    def save_json(self):
        """Save the part as json."""
        if self.part:
            self.part.dump_json()
        else:
            self.log.error("Part doesn't exist")

    def rotate(self):
        """Rotate the view."""
        if self.view:
            self.view.rotate_drawing()
        else:
            self.log.error("View doesn't exist")

    def change_shape(self):
        """Change from square/circle to the other."""
        if self.view:
            self.view.toggle_style()
        else:
            self.log.error("View doesn't exist")

    def toggle_labels(self):
        """Change from square/circle to the other."""
        if self.view:
            self.view.toggle_labels()
        else:
            self.log.error("View doesn't exist")

    def zoom_in(self):
        """Zoom in the View."""
        if self.view:
            self.view.set_zoom(1)

    def zoom_out(self):
        """Zoom out the View."""
        if self.view:
            self.view.set_zoom(-1)

    def decrease_font(self):
        """Decrease the font size."""
        if self.view:
            self.view.decrease_font()

    def increase_font(self):
        """Increase the font size."""
        if self.view:
            self.view.increase_font()

    def reset_zoom(self):
        """Zoom the View."""
        if self.view:
            self.view.reset_zoom()

    def set_properties_widget(self, widget=None) -> None:
        """Set the property widget to a new widget."""
        if self.properties.isHidden():
            self.properties.setVisible(True)
        self.properties.setWidget(widget)
