import React, { useState, useEffect, useRef } from 'react';
import "../App.css";
import Card from '../component/Card';
import Header from '../component/Header';
import { Typography, Grid, IconButton } from '@mui/material';
import { PersonOutline, AccessTimeOutlined, FlagOutlined } from '@mui/icons-material';
import SupportAgentIcon from '@mui/icons-material/SupportAgent';
import axios from 'axios';

const DetailsPage = () => {
    const [transcriptData, setTranscriptData] = useState([]);
    const effectRan = useRef(false)
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
    return (
        <>
         <Header/>
            <Card>
                <Grid container spacing={2} alignItems="center">
                    <Grid item>
                        <IconButton>
                            <SupportAgentIcon />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1">
                        John Doe
                        </Typography>
                    </Grid>
                    <Grid item>
                        <IconButton>
                            <PersonOutline />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1">
                        Alice Smith
                        </Typography>
                    </Grid>
                    <Grid item>
                        <IconButton>
                            <AccessTimeOutlined />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1">
                        2 hours
                        </Typography>
                    </Grid>
                    <Grid item>
                        <IconButton>
                            <FlagOutlined />
                        </IconButton>
                    </Grid>
                    <Grid item>
                        <Typography variant="subtitle1">
                            Negative
                        </Typography>
                    </Grid>
                    
                </Grid>
            </Card>
            <Card>
                <Grid item xs={12}>
                    <Typography variant="h6" gutterBottom>
                        Summary
                    </Typography>
                    <Typography variant="body1">
                        {transcriptData.length}
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
                </div>  
            </Card>
        </> 
    );
};

export default DetailsPage;