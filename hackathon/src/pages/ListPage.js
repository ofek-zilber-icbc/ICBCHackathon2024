import React, { useState, useEffect } from 'react';
import "../App.css";
import Card from '../component/Card';
import Header from '../component/Header';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';

const ListPage = () => {
    const [summaryDialogOpen, setSummaryDialogOpen] = useState(false);
    const [summaryText, setSummaryText] = useState('');
    const [searchValues, setSearchValues] = useState({
        representativeName: '',
        customerName: '',
        date: '',
        flag: '',
    });
    const [data, setData] = useState([]); // State variable to store the list of data
    const [filteredData, setFilteredData] = useState([]); 
    const [showNoDataMessage, setShowNoDataMessage] = useState(false);


    // Sample data
    const sampleData = [
        { representativeName: 'John Doe', customerName: 'Alice Smith', startTime: '2024-04-22 10:00 AM', endTime: '2024-04-22 10:30 AM', duration: '30 minutes', flag: 'Negative' },
        // Add more sample data as needed
    ];

    useEffect(() => {
        // Initialize data when component mounts
        setData(sampleData);
        setFilteredData(sampleData);
    }, []);

    const openSummaryDialog = (text) => {
        console.log("open")
        setSummaryText(text);
        setSummaryDialogOpen(true);
    };

    const closeSummaryDialog = () => {
        console.log("close")
        setSummaryDialogOpen(false);
    };

    const searchTable = () => {
        const filtered = data.filter(item => {
            // Filter by representative name
            if (searchValues.representativeName !== '' && !item.representativeName.toLowerCase().includes(searchValues.representativeName.toLowerCase())) {
                return false;
            }
            // Filter by customer name
            if (searchValues.customerName !== '' && !item.customerName.toLowerCase().includes(searchValues.customerName.toLowerCase())) {
                return false;
            }
            // Filter by date
            if (searchValues.date !== '' && item.startTime.split(' ')[0] !== searchValues.date) {
                return false;
            }
            // Filter by flag
            if (searchValues.flag !== '' && searchValues.flag !== 'All' && item.flag.toLowerCase() !== searchValues.flag.toLowerCase()) {
                return false;
            }
            return true;
        });
        if (filtered.length === 0) {
            setShowNoDataMessage(true);
        } else {
            setShowNoDataMessage(false);
        }
        setFilteredData(filtered);
    };

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setSearchValues({ ...searchValues, [name]: value });
    };
    const getCurrentDate = () => {
        const today = new Date();
        const year = today.getFullYear();
        let month = today.getMonth() + 1;
        let day = today.getDate();
    
        if (month < 10) {
            month = '0' + month;
        }
        if (day < 10) {
            day = '0' + day;
        }
    
        return `${year}-${month}-${day}`;
    };
    

    return (
        <>
            <Header/>
            <Card>
                <form id="filterForm" className="card-content">
                    <div className="form-group">
                        <label className="form-label">Representative Name:</label>
                        <input 
                            type="text" 
                            name="representativeName" 
                            className="form-input" 
                            placeholder="Enter name" 
                            value={searchValues.representativeName} 
                            onChange={handleInputChange} 
                        />
                    </div>
                    <div className="form-group">
                        <label className="form-label">Customer Name:</label>
                        <input 
                            type="text" 
                            name="customerName" 
                            className="form-input" 
                            placeholder="Enter name" 
                            value={searchValues.customerName} 
                            onChange={handleInputChange} 
                        />
                    </div>
                    <div className="form-group">
                        <label className="form-label">Date:</label>
                        <input 
                            type="date" 
                            name="date" 
                            className="form-input" 
                            value={searchValues.date} 
                            onChange={handleInputChange}
                            max={getCurrentDate()}  
                        />
                    </div>
                    <div className="form-group">
                        <label className="form-label">Flag:</label>
                        <select 
                            name="flag" 
                            className="form-select" 
                            value={searchValues.flag} 
                            onChange={handleInputChange}
                        >
                            <option value="">All</option>
                            <option value="positive">Positive</option>
                            <option value="negative">Negative</option>
                            <option value="neutral">Neutral</option>
                        </select>
                    </div>
                    <button type="button" className="submit-btn" onClick={searchTable}>Search</button>
                </form>
            </Card>
            {showNoDataMessage ? (
                <div className="no-data-message">No data matching the selected criteria.</div>
            ) : (
            <Card>
                <table>
                    <thead>
                        <tr>
                            <th>Representative Name</th>
                            <th>Customer Name</th>
                            <th>Start Time</th>
                            <th>End Time</th>
                            <th>Duration</th>
                            <th>Flag</th>
                            <th>Recording</th>
                            <th>Summary</th>
                            <th>Flag1</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredData.map((item, index) => (
                            <tr key={index}>
                                <td>{item.representativeName}</td>
                                <td>{item.customerName}</td>
                                <td>{item.startTime}</td>
                                <td>{item.endTime}</td>
                                <td>{item.duration}</td>
                                <td className={item.flag === 'Negative' ? 'negative-flag' : ''}>{item.flag}</td>
                                <td><a href="#">Listen</a></td>
                                <td
                                    className="summary"
                                    onClick={() => openSummaryDialog('This is a summary of the conversation.')}
                                >
                                    <a href="#">Summary</a>
                                </td>
                                <td className="flag"><a href="#">Flag </a></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </Card>
     )}
            <Dialog open={summaryDialogOpen}>
                <DialogTitle>Summary</DialogTitle>
                <DialogContent>
                    <p>{summaryText}</p>
                </DialogContent>
                <DialogActions>
                    <Button onClick={closeSummaryDialog}>Close</Button>
                </DialogActions>
            </Dialog>
        </>
    );
};

export default ListPage;
