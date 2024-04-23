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
    const [filteredData, setFilteredData] = useState([]); // State variable to store the filtered data

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
            if (searchValues.flag !== '' && item.flag !== searchValues.flag) {
                return false;
            }
            return true;
        });
        setFilteredData(filtered);
    };

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setSearchValues({ ...searchValues, [name]: value });
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
                            <th>Flag2</th>
                            <th>Flag3</th>
                            <th>Flag4</th>
                            <th>Flag5</th>
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
                                <td className="flag1"><a href="#">Flag 1</a></td>
                                <td className="flag2"><a href="#">Flag 2</a></td>
                                <td className="flag3"><a href="#">Flag 3</a></td>
                                <td className="flag4"><a href="#">Flag 4</a></td>
                                <td className="flag5"><a href="#">Flag 5</a></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </Card>
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
