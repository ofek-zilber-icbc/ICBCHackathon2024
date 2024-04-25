import React, { useState, useEffect, useRef } from 'react';
import "../App.css";
import Card from '../component/Card';
import Header from '../component/Header';
import { Typography, Grid, IconButton, Button,Dialog, DialogTitle, DialogContent, DialogActions } from '@mui/material';
import { PersonOutline, AccessTimeOutlined, FlagOutlined } from '@mui/icons-material';
import SupportAgentIcon from '@mui/icons-material/SupportAgent';
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
 
const DetailsPage = () => {
    const [transcriptData, setTranscriptData] = useState([]);
    const [transcriptExpanded, setTranscriptExpanded] = useState(false);
    const [callScore, setCallScore] = useState(0);
    const effectRan = useRef(false);
    const [showDialog, setShowDialog] = useState(false);
    const [reviewed, setReviewed] = useState(false);
    let location = useLocation();
    const navigate = useNavigate();
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('/'+location.state.short.transcriptFile);
                const displayArray = response.data.long.transcription.recognizedPhrases.filter((_, index) => index % 2 === 0);
                console.log(displayArray)
                setTranscriptData(displayArray);
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
        if (audioRef.current) {
            audioRef.current.removeEventListener('timeupdate', handleTimeUpdate);
        }
        audioRef.current.addEventListener('timeupdate', handleTimeUpdate);
        return () => {
            if (audioRef.current) {
                audioRef.current.removeEventListener('timeupdate', handleTimeUpdate);
            }
            audioRef.current.removeEventListener('timeupdate', handleTimeUpdate);
        };
    }, []);
 
    const handleTranscriptClick = (startTime) => {
        audioRef.current.currentTime = startTime;
        console.log(location.state.flags)
    };
    const handleMarkAsReviewed =() =>{
        setReviewed(!reviewed);
    }
    const handleBackButtonClick = () => {
        navigate(-1); // Go back in history
    };
    const handleReprocessButtonClick = () => {
        setShowDialog(true);
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
            <Grid container justifyContent="space-between" alignItems="center">
                <Grid item style={{ fontWeight: 'bold' }}>
                    <Typography variant="h5" style = {{paddingBottom: "10px"}}>
                         Call Details
                    </Typography>
                </Grid>
            <Grid item style={{ fontWeight: 'bold' }}>
                    <Button variant="contained" onClick={handleMarkAsReviewed} style={{ borderRadius: "10px", background: reviewed ? "grey" : "#4CBB17" }}>
                        {reviewed ? "Mark as Needs Review" : "Mark as Reviewed"}
                    </Button>
            </Grid>
            </Grid>
                <Grid container spacing={0.5} alignItems="center">
                    <Grid item>
                        <IconButton style={{ color: '#8526FF' }}>
                            <SupportAgentIcon />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1" marginRight={"15px"}>
                        {location.state.short.representativeName}
                        </Typography>
                    </Grid>
                    <Grid item>
                        <IconButton style={{ color: '#8526FF' }}>
                            <PersonOutline />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1" marginRight={"15px"}>
                        {location.state.short.customerName}
                        </Typography>
                    </Grid>
                    <Grid item>
                        <IconButton style={{ color: '#8526FF' }}>
                            <AccessTimeOutlined />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1" marginRight={"15px"}>
                        {location.state.short.callLength} mins
                        </Typography>
                    </Grid>
                    <Grid item>
                        <IconButton style={{ color: '#8526FF' }}>
                            <FlagOutlined />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1" marginRight={"10px"}>
                            {location.state.short.flags.length == 0 ? "No flags" : `Flags: ${location.state.short.flags.length}`}
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
                <Grid container spacing={0.5} alignItems="center">
                    <Typography>
                        {/* {location.state.flags[1].timestamp} */}
                    </Typography>
                    </Grid>
            </Card>
            <Card>
                <div>
                    <audio ref={audioRef} controls>
                        <source src={location.state.long.transcription.source} type="audio/wav" />
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
                <div
                    key={index}
                    style={{
                        backgroundColor:
                        currentTime >= word.offsetInTicks / 10000000 &&
                        currentTime <= (word.offsetInTicks + word.durationInTicks) / 10000000
                         ? 'yellow'
                        : 'transparent',
                        color: word.nBest[0].sentiment.negative >= 0.85 ? 'red' : 'inherit', // Change text color to red if sentiment is negative
                        cursor: 'pointer',
                    }}
                    onClick={() => handleTranscriptClick(word.offsetInTicks / 10000000)}
                >
                {word.nBest[0].display}{' '}
                </div>
               
                 ))}
                </div>
                )}
                </div>  
            </Card>
            <div style={{ display: 'flex', justifyContent: 'flex-end', paddingRight: '20px', background:"#EFEFEF",paddingTop:"40px", paddingBottom:"100px", paddingRight:"40px" }}>
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
                border: '2px solid #8526FF',
                }}
            >
                Back
            </Button>
            <Button
                type="button"
                onClick={handleReprocessButtonClick}
                sx={{
                    bgcolor: '#8526FF',
                    color: 'white',
                    '&:hover': {
                     bgcolor: '#5d1a9e',
                    },
                borderRadius: '30px',
                padding: '5px 50px',
                margin: '5px',
                border: '2px solid #8526FF',
                }}
            >
                Reprocess this call
            </Button>
            </div>
            <Dialog open={showDialog} onClose={() => setShowDialog(false)}>
                <DialogTitle>Reprocess Call</DialogTitle>
                <DialogContent>
                    <Typography>We have sent your request to reprocess this call.</Typography>
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => setShowDialog(false)} color="primary" autoFocus>
                        OK
                    </Button>
                </DialogActions>
            </Dialog>      
        </>
    );
};
 
export default DetailsPage;