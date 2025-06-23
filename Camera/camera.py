from mcp.server.fastmcp import FastMCP
import cv2
import os

mcp = FastMCP("camera", timeout=600)

@mcp.tool()
def capturePhoto(path: str, show: bool = False, name: str = "captured_photo.jpg", time: int = 5000) -> str:
    cam = cv2.VideoCapture(0)
    _ , frame = cam.read()
    if _ :
        success = cv2.imwrite(os.path.join(path, name), frame)
        cam.release()
        if not success:
            raise RuntimeError("Failed to write image to specified path")
        if show:
            cv2.imshow("Hello", frame)
            cv2.waitKey(time)
            cv2.destroyAllWindows()
            return "Successfully captured and displayed image"
        else:
            return "Successfully captured the image"
    else :
        cam.release()
        raise RuntimeError("Error occured while opening camera")

if __name__ == "__main__":
    mcp.run(transport="stdio")