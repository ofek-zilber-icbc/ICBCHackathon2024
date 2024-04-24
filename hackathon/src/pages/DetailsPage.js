import React, { useState } from 'react';
import "../App.css";
import Card from '../component/Card';
import Header from '../component/Header';

const DetailsPage = () => {
   
    return (
        <>
            <Header/>
            <Card>
                <div className="details-container">
                    <div>
                        <strong>Customer Name:</strong> John Doe
                    </div>
                    <div>
                        <strong>Representative Name:</strong> Jane Smith
                    </div>
                
                    <div>
                        <strong>Duration:</strong> 35 minutes
                    </div>
                    <div>
                        <strong>Flag:</strong> Negative
                    </div>
                </div>
        
            </Card>
            <Card>
            <div>
            <h2>Audio Player</h2>
            <audio controls>
                <source src="/case2.m4a" type="audio/mpeg" />
                Your browser does not support the audio element.
            </audio>
        </div>
                  
            </Card>
        </> 
    );
};

export default DetailsPage;