import React, { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";
import "./styles.css";

const WebCamComponent = () => {

    const [isCapturing, setIsCapturing] = useState<boolean>(false);
    const webcamRef = useRef<Webcam>(null);
    const [picture, setPicture] = useState<string | null>(null);

    const getScreenshotWebcam = useCallback(() => {
        const imageTaken = webcamRef.current?.getScreenshot();
        if (imageTaken) {
            setPicture(imageTaken);
        }
    }, [webcamRef]);


    return (
        <div className="webcam-container">
            {!isCapturing && (
                <div className="welcome-btn-container" >
                    <button className="welcome-btn" onClick={() => setIsCapturing(true)}>Get started!</button>
                </div>
            )}
            {isCapturing && (
                <div className="welcome-btn-container" style={{flexDirection: "row"}}>
                    <div>
                        <button onClick={() => setIsCapturing(false)}>Exit</button>
                    </div>
                    <div>
                        <Webcam
                            audio={false}
                            width={500}
                            height={500}
                            ref={webcamRef}
                            screenshotFormat="image/jpeg"
                        />
                    </div>
                    <div>
                        <button onClick={getScreenshotWebcam}>Take picture</button>
                    </div>
                </div>
                
            )}
            {picture && (
                <div className="welcome-btn-container" style={{ flexDirection: "row" }}>
                    <div>
                        <button
                            onClick={() => {
                                setPicture(null);
                            }}
                        >
                            delete
                        </button>
                    </div>
                    <div>
                        <img src={picture} alt="Screenshot" />
                    </div>
                </div>
            )}
        </div>
    )

}

export default WebCamComponent;