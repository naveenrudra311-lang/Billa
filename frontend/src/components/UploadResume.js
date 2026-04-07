import React from "react"
import axios from "axios"

function UploadResume(){

const upload = async(e)=>{

const file = e.target.files[0]

const formData = new FormData()

formData.append("file",file)

await axios.post(
"http://localhost:8000/upload-resume",
formData
)

alert("Resume Uploaded")

}

return(

<div>

<h2>Upload Resume</h2>

<input type="file" onChange={upload}/>

</div>

)

}

export default UploadResume