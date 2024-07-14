# TODO: may want to abstract this to data-producing device_implementations in general, not just cameras
from typing import Iterable, Optional, Union
from dataclasses import dataclass, field
import itertools
from pycromanager.execution_engine.kernel.acq_event_base import AcquisitionEvent, DataProducing, Stoppable
from pycromanager.execution_engine.kernel.device_types_base import Camera
from pycromanager.execution_engine.kernel.data_coords import DataCoordinates


@dataclass
class ReadoutImages(AcquisitionEvent, DataProducing, Stoppable):
    """
    Readout one or more images (and associated metadata) from a camera

    Attributes:
        num_images (int): The number of images to read out. If None, the readout will continue until the
            image_coordinate_iterator is exhausted or the camera is stopped and no more images are available.
        camera (Camera): The camera object to read images from.
        stop_on_empty (bool): If True, the readout will stop when the camera is stopped when there is not an
            image available to read
        image_coordinate_iterator (Iterable[DataCoordinates]): An iterator or list of ImageCoordinates objects, which
            specify the coordinates of the images that will be read out, should be able to provide at least num_images
            elements.
    """
    camera: Optional[Union[Camera, str]] = field(default=None)
    # TODO: should this change to a buffer object?
    num_images: int = field(default=None)
    stop_on_empty: bool = field(default=False)

    def execute(self) -> None:
        # TODO a more efficient way to do this is with callbacks from the camera
        #  but this is not currently implemented, at least for Micro-Manager cameras
        image_counter = itertools.count() if self.num_images is None else range(self.num_images)
        for image_number, image_coordinates in zip(image_counter, self.image_coordinate_iterator):
            while True:
                # check if event.stop has been called
                if self.is_stop_requested():
                    return
                image, metadata = self.camera.pop_image(timeout=0.01) # only block for 10 ms so stop event can be checked
                if image is None and self.stop_on_empty:
                    return
                elif image is not None:
                    self.put_data(image_coordinates, image, metadata)
                    break



@dataclass
class StartCapture(AcquisitionEvent):
    """
    Special device instruction that captures images from a camera
    """
    num_images: int
    camera: Optional[Camera]

    def execute(self):
        """
        Capture images from the camera
        """
        try:
            self.camera.arm(self.num_images)
            self.camera.start()
        except Exception as e:
            self.camera.stop()
            raise e

@dataclass
class StartContinuousCapture(AcquisitionEvent):
    """
    Tell data-producing device to start capturing images continuously, until a stop signal is received
    """
    camera: Optional[Camera]

    def execute(self):
        """
        Capture images from the camera
        """
        try:
            self.camera.arm()
            self.camera.start()
        except Exception as e:
            self.camera.stop()
            raise e

@dataclass
class StopCapture(AcquisitionEvent):
    """
    Tell data-producing device to start capturing images continuously, until a stop signal is received
    """
    camera: Optional[Camera]

    def execute(self):
        self.camera.stop()
