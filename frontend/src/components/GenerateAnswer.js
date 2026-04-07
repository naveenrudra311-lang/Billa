import React,{useState} from "react"
import axios from "axios"

function GenerateAnswer(){

const [question,setQuestion]=useState("")
const [answer,setAnswer]=useState("")

const generate = async()=>{

const res = await axios.post(
"http://localhost:8000/generate-answer",
null,
{params:{question}}
)

setAnswer(res.data.answer)

}

return(

<div>

<h2>Interview Question</h2>

<input
style={{width:"400px"}}
placeholder="Ask question"
onChange={(e)=>setQuestion(e.target.value)}
/>

<button onClick={generate}>
Generate Answer
</button>

<pre>{answer}</pre>

</div>

)

}

export default GenerateAnswer