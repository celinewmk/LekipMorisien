import React, { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";
import "./styles.css";
import axios from 'axios';

const WebCamComponent = () => {

    const launchLabel = "GET STARTED!";
    const exitLabel = "GO BACK TO MAIN PAGE"
    const takePictureLabel = "TAKE SCREENSHOT"

    const [openCamera, setOpenCamera] = useState<boolean>(false);
    const webcamRef = useRef<Webcam>(null);
    const [picture, setPicture] = useState<string | null>(null);

    const getScreenshotWebcam = useCallback(() => {
        const imageTaken = webcamRef.current?.getScreenshot();
        if (imageTaken) {
            setPicture(imageTaken);

            const base64EncodedImage = imageTaken.replace(/^data:image\/(png|jpg|jpeg);base64,/, "");

            try {
                axios({
                    method: 'get',
                    url: "https://vgssadiquawneydqm5nvaejw4i0rfjio.lambda-url.us-east-1.on.aws/",
                }).then(response => {
                    console.log(response.data);
                });
               
            } catch (error) {
                console.error(error);
            }
        }

        
    }, [webcamRef]);

    return (
        <div className="container">
            {!openCamera && (
                <div className="welcome-btn-container" >
                    <button className="btn" onClick={() => setOpenCamera(true)}>{launchLabel}</button>
                </div>
            )}
            {openCamera && (
                <div style={{ display: "flex", justifyContent: "center", alignItems: "center", flexDirection: "column"}}>
                    <div className="webcam-container">
                        <Webcam
                            audio={false}
                            width={500}
                            height={500}
                            ref={webcamRef}
                            screenshotFormat="image/jpeg"
                            mirrored={true}
                        />
                    </div>
                    {/* <div className="overlay">
                        <img alt="grid" src={require('./images/grid.png')} />
                    </div> */}
                    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", flexDirection: "column" }}>
                        <button className="btn" onClick={getScreenshotWebcam}>{takePictureLabel}</button>
                        <button className="btn" style={{marginTop: 20}} onClick={() => setOpenCamera(false)}>{exitLabel}</button>   
                    </div>
                </div>
                
            )}
            {picture && (
                <div style={{marginTop: 5}}>
                    <img style={{padding: 10}} src={picture} alt="Screenshot" />
                    <div>
                        <button onClick={() => {setPicture(null)}}  className="btn">
                            delete
                        </button>
                    </div>
                </div>
            )}
        </div>
    )

}

export default WebCamComponent;