import React, { useState, useEffect } from 'react';
import "../App.css";
import Card from '../component/Card';
import Header from '../component/Header';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';
import DataTable from './data-table';




const ListPage = () => {

    const[records, setRecords] = useState([])

    // useEffect(() => {
    //     fetch('https://hackathonintegrarion.azurewebsites.net/api/httpintegration?code=qFOvl6g0buD_FfrqyA1SqhQQ07DlPsHj3ca_v_WEQRjvAzFudoirjw%3D%3D')
    //     .then(res => res.json())
    //     .then(data => {
    //         setRecords(data.calls)
    //     })
    // }, [])

    useEffect(() => {
        fetch('https://66262d51052332d55321e99a.mockapi.io/calls')
        .then(res => res.json())
        .then(data => {
            setRecords(data)
        })
    }, [])

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
                    <DataTable records={records}/>
                    <Dialog open={summaryDialogOpen}>
                        <DialogTitle>Summary</DialogTitle>
                        <DialogContent>
                            <p>{summaryText}</p>
                        </DialogContent>
                        <DialogActions>
                            <Button onClick={closeSummaryDialog}>Close</Button>
                        </DialogActions>
                    </Dialog>
                </Card>
            
            )}
        </>
    );
};

export default ListPage;