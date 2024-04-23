import React from 'react';
import "../App.css"
const Header = () => {
    return (
        <div className="container">
            <div className="left-divs">
                <div className="left-div"><img src="http://confluence/download/attachments/65571/atl.site.logo?version=3&modificationDate=1572388452267&api=v2" alt="ICBC" className="LOGO"/></div>
                <div className="left-div Title">Call Center Analysis Platform</div>
            </div>
            <div className="right-divs">
                <div className="right-div text">Hello, Bella</div>
                <div className="right-div text">Logout</div>
            </div>
        </div>
    );
};

export default Header;