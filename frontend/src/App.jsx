import { useEffect,useState} from "react";
import axios from "axios";

function App()
{
  const [tasks,setTasks]=useState([]);
  const[title,setTitle]=useState("");

  const API="http://127.0.0.1:8000";

  const fetchTasks=async()=>
  {
    const res=await axios.get(`${API}/todo`);
    setTasks(res.data);
  };

  useEffect(()=>
  {
    fetchTasks();
  },[]);

  const addTask=async()=>{
    if(!title)
      return;
    await axios.post(`${API}/todo`,{title});
    setTitle("");
    fetchTasks();
  };

  const markDone=async(id)=>
  {
    try
    {
      await axios.put(`${API}/todo/${id}`);
      await fetchTasks();
    }
    catch(err)
    {
      console.error("Error marking done: ",err);
    }
  };

  const deleteTask=async(id)=>
  {
    try {
    await axios.delete(`${API}/todo/${id}`);
    await fetchTasks();
  } catch (err) {
    console.error("Error deleting task: ",err);
  }
  }

  return (
    <div style ={{padding: "25px"}}>
      <h1>TODO App</h1>

      <input value={title} onChange={(e)=>setTitle(e.target.value)} placeholder="New Task"/>
      <button onClick={addTask}>ADD</button>

      <ul>
        {tasks.map((task)=>(
          <li key={task.id}>
            {task.completed?"✅":"⬜"}{task.title}

            {!task.completed&&(<button onClick={()=>markDone(task.id)} style={{marginLeft:"10px"}}>
              Done
            </button>)}

            <button onClick={()=>deleteTask(task.id)} style={{marginLeft:"20px"}}>
              Delete
              </button>
          </li>
        ))}
      </ul>
    </div> 
  );
}
export default App;
