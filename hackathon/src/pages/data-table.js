import React from 'react'
import { useEffect, useState } from 'react'
import "../App.css";
import { BrowserRouter } from 'react-router-dom';
import { Link } from 'react-router-dom';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';


const DataTable = (props) => {
    const [summaryDialogOpen, setSummaryDialogOpen] = useState(false);
    const [summaryText, setSummaryText] = useState('');

   // Function to open the summary dialog
   const openSummaryDialog = (text) => {
        console.log("open")
        setSummaryText(text);
        setSummaryDialogOpen(true);




        
    };
    // Function to close the summary dialog
    const closeSummaryDialog = () => {
        console.log("close")
        setSummaryDialogOpen(false);
    };
    return (
        <>
            <table>
                <thead>
                    <tr>
                        <th>Representative Name</th>
                        <th>Customer Name</th>
                        <th>Summary</th>
                        <th>Date</th>
                        <th>Call Length</th> 
                        <th>Flag</th>
                        <th>Details</th>
                        <th>Rviewed</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        props.records.map((record, i) => {
                            const getFlagClassName = (flags) => {
                                return flags.length === 0 ? 'non-negative-flag' : 'negative-flag';
                            };
                        
                            const getFlagText = (flags) => {
                                return flags.length === 0 ? 'Non-negative' : 'Negative';
                            };
                            return (
                            <tr key={i}>
                                <td>{record.short.representativeName}</td>
                                <td>{record.short.customerName}</td>
                                <td
                                    className="summary"
                                    onClick={() => openSummaryDialog(record.short.summary)}
                                >
                                    <a href="#">Summary</a>
                                </td>                              
                                <td>{record.short.date}</td>
                                <td>{record.short.callLength + "mins"}</td>
                                <td className={getFlagClassName(record.short.flags)}>{getFlagText(record.short.flags)}</td>
                                <td><Link to='/details' state={record}>Show details</Link></td> 
                                <td>Reviewed</td>
                            </tr>)
                        })
                    }
                </tbody>
            </table>
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
    )
}

export default DataTable
