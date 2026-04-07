import React from "react";
import UploadResume from "./components/UploadResume";
import GenerateAnswer from "./components/GenerateAnswer";

function App(){

return(

<div style={{padding:"40px"}}>

<h1>Interview AI Assistant</h1>

<UploadResume/>

<hr/>

<GenerateAnswer/>

</div>

)

}

export default App