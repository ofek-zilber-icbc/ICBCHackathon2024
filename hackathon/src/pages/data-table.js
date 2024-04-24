import React from 'react'
import { useEffect, useState } from 'react'
import "../App.css";


const DataTable = (props) => {
    
    return (
            <table>
                <thead>
                    <tr>
                        <th>Representative Name</th>
                        <th>Customer Name</th>
                        {/* <th>Transcription</th> */}
                        <th>Summary</th>
                        <th>Date</th> 
                        <th>Call Length</th>
                        <th>Flag</th>
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
                                <td>{record.representativeName}</td>
                                <td>{record.customerName}</td>
                                {/* <td>{record.transcription}</td> */}
                                <td>{record.summary}</td>
                                <td>{record.date}</td>
                                {/* <td className={record.flag === 'Negative' ? 'negative-flag' : ''}>{record.flag}</td>    */}
                                <td>{record.callLength + "mins"}</td>
                                <td className={getFlagClassName(record.flags)}>{getFlagText(record.flags)}</td>
                            </tr>)
                        })
                    }
                </tbody>
            </table>
      
    )
}

export default DataTable
