import React from 'react';
import "../App.css"
const Card = ({children}) => {
    return (
        <div className="card-container">
            <div className="card">
               {children}
            </div>
        </div>
    );
};

export default Card;