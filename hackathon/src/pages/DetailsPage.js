import React, { useState, useEffect, useRef } from 'react';
import "../App.css";
import Card from '../component/Card';
import Header from '../component/Header';
import { Typography, Grid, IconButton, Button} from '@mui/material';
import { PersonOutline, AccessTimeOutlined, FlagOutlined } from '@mui/icons-material';
import SupportAgentIcon from '@mui/icons-material/SupportAgent';
import axios from 'axios';
import { useLocation } from 'react-router-dom';

const DetailsPage = () => {
    const [transcriptData, setTranscriptData] = useState([]);
    const [transcriptExpanded, setTranscriptExpanded] = useState(false); 
    const [callScore, setCallScore] = useState(0); 
    const effectRan = useRef(false)
    let location = useLocation();
    console.log("location", location.state.representativeName)
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('/batch.json');
                const recognizedPhrases = response.data.recognizedPhrases || [];
                const newDisplayWords = recognizedPhrases.reduce((acc, phrase) => {
                    if (phrase.nBest[0].displayWords !== undefined) {
                        const newWords = phrase.nBest[0].displayWords;
                        console.log("new word", newWords)
                        return [...acc, ...newWords];
                    }
                    return acc;
                }, []);
                console.log("END!!!!!!!!!!!!!")
                setTranscriptData(newDisplayWords);
            } catch (error) {
                console.error('Error fetching JSON:', error);
            }
        };
        fetchData();
    }, []);


    const [currentTime, setCurrentTime] = useState(0);
    const audioRef = useRef(null);

    useEffect(() => {
        const handleTimeUpdate = () => {
            setCurrentTime(audioRef.current.currentTime);
        };
        audioRef.current.addEventListener('timeupdate', handleTimeUpdate);
        return () => {
            audioRef.current.removeEventListener('timeupdate', handleTimeUpdate);
        };
    }, []);

    const handleTranscriptClick = (startTime) => {
        audioRef.current.currentTime = startTime;
    };
    const handleBackButtonClick = () => {
    };
    const toggleTranscript = () => {
        setTranscriptExpanded(!transcriptExpanded);
    };
    const calculateCallScore = () => {
        // Your logic to calculate call score goes here
        // For now, let's assume call score is a random number between 0 and 100
        return Math.floor(Math.random() * 101); // Random number between 0 and 100
    };
    useEffect(() => {
        // Calculate call score when component mounts
        const score = calculateCallScore();
        setCallScore(score);
    }, []);
    return (
        <>
         <Header/>
            <Card>
                <Grid item style={{ fontWeight: 'bold', marginBottom: '10px' }}>
                    <Typography variant="h5" fontWeight={"bold"}>
                        Call Details
                    </Typography>
                </Grid>
                <Grid item style={{ fontWeight: 'bold', marginBottom: '10px' }}>
                    <div style={{ display: 'flex', justifyContent: 'flex-end', paddingRight: '20px'}}>
                        <Typography variant="h7" color="white" style={{ background: "#8526FF", padding: "10px", borderRadius: "10px" }}>
                            Call Score: {callScore}
                        </Typography>
                    </div> 
                </Grid>
                <Grid container spacing={0.5} alignItems="center">
                    <Grid item>
                        <IconButton style={{ color: '#8526FF' }}>
                            <SupportAgentIcon />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1" marginRight={"15px"}>
                        {/* John Doe */}
                        {location.state.representativeName}
                        </Typography>
                    </Grid>
                    <Grid item>
                        <IconButton style={{ color: '#8526FF' }}>
                            <PersonOutline />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1" marginRight={"15px"}>
                        {location.state.customerName}
                        </Typography>
                    </Grid>
                    <Grid item>
                        <IconButton style={{ color: '#8526FF' }}>
                            <AccessTimeOutlined />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1" marginRight={"15px"}>
                        {location.state.callLength} mins
                        </Typography>
                    </Grid>
                    <Grid item>
                        <IconButton style={{ color: '#8526FF' }}>
                            <FlagOutlined />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1" marginRight={"10px"}>
                            Negative
                        </Typography> 
                    </Grid> 
                </Grid>
                <Grid item xs={12}>
                    <Typography variant="h6" gutterBottom marginTop={"30px"} fontWeight={"bold"}>
                        Summary
                    </Typography>
                    <Typography variant="body1">
                    A representative contacted the customer regarding their treatment and injury claim. They discussed the importance of following up with their physiotherapist and adhering to the treatment plan. The customer acknowledged the need for action and agreed to contact the physiotherapist. The representative emphasized timely communication and urged the customer to call back promptly. The conversation concluded with the customer committing to follow up and thanking the representative for their assistance.
                    </Typography>
                </Grid>
            </Card>
            <Card>
                <div>
                    <audio ref={audioRef} controls>
                        <source src="/call2.m4a" type="audio/mpeg" />
                        Your browser does not support the audio element.
                    </audio>
                <div>
                    <Button onClick={toggleTranscript}>
                        {transcriptExpanded ? 'Collapse Transcript' : 'Expand Transcript'}
                    </Button>
                </div>

                {transcriptExpanded && (
                    <div>
                        {transcriptData!== null && transcriptData.map((word, index) => (
                            <span
                                key={index}
                                style={{
                                    backgroundColor:
                                        currentTime >= word.offsetInTicks / 10000000 &&
                                        currentTime <= (word.offsetInTicks + word.durationInTicks) / 10000000
                                            ? 'yellow'
                                            : 'transparent',
                                    cursor: 'pointer',
                                }}
                                onClick={() => handleTranscriptClick(word.offsetInTicks / 10000000)}
                            >
                                {word.displayText}{' '}
                            </span>
                        ))}
                    </div>
                )}
                </div>  
            </Card>
            <div style={{ display: 'flex', justifyContent: 'flex-end', paddingRight: '20px' }}>
            <Button 
                type="button" 
                onClick={handleBackButtonClick} 
                sx={{
                    bgcolor: 'white',
                    color: '#8526FF',
                    '&:hover': {
                     bgcolor: '#5d1a9e',
                    },
                borderRadius: '30px',
                padding: '5px 50px',
                margin: '5px',
                border: '2px solid #8526FF', 
                }}
            >
                Back
            </Button>
            </div>       
        </> 
    );
};

export default DetailsPage;