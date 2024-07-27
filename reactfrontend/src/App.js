import './App.css';
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [ words, setWords ] = useState([])
  useEffect(()=>{
    async function getAllWords(){
      try {
        const words = await axios.get("http://127.0.0.1:8000/api/item/")
        console.log(words.data)
        setWords(words.data)
      } catch (error) {
        console.log(error)
        }
    }
    getAllWords()
    }, [])
  return (
    <div className="App">
      <h1>Connect Reactjs to Django Backends</h1>
      {
        words.map((word, i)=>{
          return (
          <h2 key={i}>{word.word} {word.wordTrans}</h2>
          )
        })
      }
    </div>
  );
}

export default App;
