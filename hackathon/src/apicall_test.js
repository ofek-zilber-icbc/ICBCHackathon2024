import React from 'react'


async function apicall() {
    const response = await fetch('https://hackathonintegrarion.azurewebsites.net/api/httpintegration?code=qFOvl6g0buD_FfrqyA1SqhQQ07DlPsHj3ca_v_WEQRjvAzFudoirjw%3D%3D')
    const data = await response.json()
    return data
}

const ApiCallTest = () => {

    const data = apicall()

    console.log(data)

  return (
    <div>
      
    </div>
  )
}

export default ApiCallTest
