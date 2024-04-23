import React, { useState } from 'react';
import "../App.css";
import Card from '../component/Card';
import Header from '../component/Header';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';

const ListPage = () => {
    const [summaryDialogOpen, setSummaryDialogOpen] = useState(false);
    const [summaryText, setSummaryText] = useState('');

    const openSummaryDialog = (text) => {
        console.log("open")
        setSummaryText(text);
        setSummaryDialogOpen(true);
    };

    const closeSummaryDialog = () => {
        console.log("close")
        setSummaryDialogOpen(false);
    };
    return (
        <>
            <Header/>
                <Card>
                        <form id="filterForm" className="card-content">
                            <div className="form-group">
                                <label  className="form-label">Representative Name:</label>
                                <input type="text" id="name" className="form-input" placeholder="Enter name" />
                            </div>
                            <div className="form-group">
                                <label  className="form-label">Customer Name:</label>
                                <input type="text" id="name" className="form-input" placeholder="Enter name" />
                            </div>
                            <div className="form-group">
                                <label  className="form-label">Date:</label>
                                <input type="date" id="date" className="form-input" />
                            </div>
                            <div className="form-group">
                                <label  className="form-label">Flag:</label>
                                <select id="type" className="form-select">
                                    <option value="1">positive</option>
                                    <option value="2">negative</option>
                                    <option value="3">neutral</option>
                                </select>
                            </div>
                            <button type="submit" className="submit-btn">Search</button>
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
                            {/* Sample data rows */}
                            <tr>
                                <td>John Doe</td>
                                <td>Alice Smith</td>
                                <td>2024-04-22 10:00 AM</td>
                                <td>2024-04-22 10:30 AM</td>
                                <td>30 minutes</td>
                                <td className="negative-flag">Negative</td>
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
                            {/* Add more rows as needed */}
                        </tbody>
                    </table>

            {/* Summary Dialog */}
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
        </> 
    );
};

export default ListPage;