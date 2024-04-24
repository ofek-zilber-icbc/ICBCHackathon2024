import React from 'react'
import { useEffect, useState } from 'react'


const DataTable = () => {
    const[records, setRecords] = useState([])

    useEffect(() => {
        fetch('https://hackathonintegrarion.azurewebsites.net/api/httpintegration?code=qFOvl6g0buD_FfrqyA1SqhQQ07DlPsHj3ca_v_WEQRjvAzFudoirjw%3D%3D')
        .then(res => res.json())
        .then(data => {
            setRecords(data.calls)
        })
    }, [])

    // temporary
    // useEffect(() => {
    //     fetch('https://66262d51052332d55321e99a.mockapi.io/calls')
    //     .then(res => res.json())
    //     .then(data => {
    //         setRecords(data)
    //     })
    // }, [])

    
    console.log("records: ", records)

    records.map((record) => {
        console.log("name", record.customerName)
    })
    
    return (
            <table>
                <thead>
                    <tr>
                        <th>Representative Name</th>
                        <th>Customer Name</th>
                        <th>Transcription</th>
                        <th>Summary</th>
                        {/* <th>Flag</th>    */}
                        <th>Call Length</th>
                        {/* <th>Date</th>    */}
                    </tr>
                </thead>
                <tbody>
                    {
                        records.map((record, i) => {
                            return (
                            <tr key={i}>
                                <td>{record.representative}</td>
                                <td>{record.customerName}</td>
                                <td>{record.transcription}</td>
                                <td>{record.summary}</td>
                                {/* <td className={record.flag === 'Negative' ? 'negative-flag' : ''}>{record.flag}</td>    */}
                                {/* <td className='negative-flag'>Negative</td> */} 
                                <td>{record.callLength}</td>
                                {/* <td>{record.date}</td>    */}
                            </tr>)
                        })
                    }
                </tbody>
            </table>
      
    )
}

export default DataTable
