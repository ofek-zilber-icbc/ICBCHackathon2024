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
                        <th>Transcription</th>
                        <th>Summary</th>
                        <th>Flag</th>   
                        <th>Call Length</th>
                        <th>Date</th>   
                    </tr>
                </thead>
                <tbody>
                    {
                        props.records.map((record, i) => {
                            return (
                            <tr key={i}>
                                <td>{record.representative}</td>
                                <td>{record.customerName}</td>
                                <td>{record.transcription}</td>
                                <td>{record.summary}</td>
                                {/* <td className={record.flag === 'Negative' ? 'negative-flag' : ''}>{record.flag}</td>    */}
                                <td className='negative-flag'>Negative</td> 
                                <td>{record.callLength}</td>
                                <td>{record.date}</td>   
                            </tr>)
                        })
                    }
                </tbody>
            </table>
      
    )
}

export default DataTable
