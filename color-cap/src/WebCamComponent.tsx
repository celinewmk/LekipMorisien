import React, { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";
import "./styles.css";
import { BsArrowRepeat, BsHouseDoorFill } from "react-icons/bs";
import { AiFillInfoCircle, AiFillSound } from "react-icons/ai"
import axios from 'axios';

const WebCamComponent = () => {

    const launchLabel = "START!";
    const takePictureLabel = "CAPTURE"

    const [exactColor, setExactColor] = useState<string | null>(null);
    const [closestColor, setClosestColor] = useState<string | null>(null);

    const [openCamera, setOpenCamera] = useState<boolean>(false);
    const webcamRef = useRef<Webcam>(null);
    const [picture, setPicture] = useState<string | null>(null);

    const [showModal, setShowModal] = useState<boolean>(false);

    const getScreenshotWebcam = useCallback(() => {
        const imageTaken = webcamRef.current?.getScreenshot();
        if (imageTaken) {
            setPicture(imageTaken);

            const base64EncodedImage = imageTaken.replace(/^data:image\/(png|jpg|jpeg);base64,/, "");
            const url = "https://n2c5bmex9j.execute-api.us-east-1.amazonaws.com/HackTheHill";
            const body = { image: base64EncodedImage };

            try {
                let config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    }
                }
                axios.post(url, body, config).then(response => {
                        const { exact, next_closest } = JSON.parse(response.data.body);
                        console.log(exact, next_closest);
                        setExactColor(`Exact Color: ${exact}`);
                        setClosestColor(`Closest Color: ${next_closest}`);
                    });
            } catch (error) {
                console.error(error);
            }
        }
    }, [webcamRef]);

    const goBackToHome = () => {
        setOpenCamera(false)
        setPicture(null)
        setShowModal(false)
    }

    const retry = () => {
        setPicture(null)
        setShowModal(false)
    }

    const tts = () => {
        let utterance = new SpeechSynthesisUtterance(`${exactColor}. ${closestColor}`);
        speechSynthesis.speak(utterance);
    }

    return (
        <div className="container">
            {!openCamera && (
                <div className="welcome-btn-container" >
                    <button className="btn" onClick={() => setOpenCamera(true)}>{launchLabel}</button>
                </div>
            )}
            {openCamera && picture === null && (
                <div className="webcam-container">
                    <div className="webcam">
                        <Webcam
                            audio={false}
                            width={700}
                            height={500}
                            ref={webcamRef}
                            screenshotFormat="image/jpeg"
                            mirrored={true}
                        />
                        <div className="overlay">
                            <img alt="grid" src={require('./images/grid.png')} height={"90%"} width={"90%"} />
                        </div>
                    </div>
                    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", flexDirection: "row" }}>
                        <button className="btn" onClick={getScreenshotWebcam}>{takePictureLabel}</button>
                        <BsHouseDoorFill onClick={goBackToHome} size={"30px"} style={{ cursor: "pointer", padding: 35}} />
                    </div>
                </div>
                
            )}
            {picture && (
                <div style={{marginTop: "40px"}}>
                    <div className="result-container">
                        <p className="result-text">{exactColor}</p>
                        <p className="result-text">{closestColor}</p>
                        <AiFillSound onClick={() => tts()} size={"30px"} className="text-to-speech-icon" color="white" />
                    </div>
                    {showModal && (
                        <div className="modal-container">
                            <p style={{textAlign: "center"}}>This is a detailed description of the exact color. </p>
                        </div>
                    )}
                    
                    <img style={{marginTop: 10}} src={picture} alt="Screenshot" height={500} width={700} />
                    <div style={{ display: "flex", justifyContent: "center" }}>
                        <BsHouseDoorFill onClick={() => goBackToHome()} size={"30px"} style={{ cursor: "pointer", padding: 15}} />
                        <BsArrowRepeat onClick={() => retry()} size={"30px"} style={{ cursor: "pointer", padding: 15}} />
                        <AiFillInfoCircle onClick={() => setShowModal(!showModal)} size={"30px"} style={{ cursor: "pointer", padding: 15}}/>
                    </div>
                </div>
            )}
        </div>
    )

}

export default WebCamComponent;