import axios from "axios";
import { useEffect, useState } from "react";

interface Task {
  id: number;
  title: string;
  category: string;
  isDone: boolean;
  dateCreated: string;
}

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    axios
      .get<Task[]>("http://127.0.0.1:8000/toDos")
      .then((res) => setTasks(res.data));
  }, []);

  return (
    <div className="w-screen h-screen flex flex-col justify-center items-center">
      <h1 className="text-5xl my-4  text-blue-500">To do list</h1>
      <div className="w-1/2 h-1/2">
        <table className="text-center w-full table-fixed">
          <thead>
            <tr className="text-xl bg-blue-500 text-white">
              <th className="p-2">ID</th>
              <th>Title</th>
              <th>Category</th>
              <th>Date</th>
              <th>Completed</th>
            </tr>
          </thead>
          <tbody>
            {tasks.map((task) => (
              <tr key={task.id}>
                <td className="bg-blue-200 font-semibold p-2">{task.id}</td>
                <td className="bg-blue-100">{task.title}</td>
                <td className="bg-blue-200">{task.category}</td>
                <td className="bg-blue-100">{task.dateCreated}</td>
                <td className="bg-blue-200  w-4 h-4">
                  {task.isDone ? (
                    <input
                      className="w-4 h-4 rounded-none"
                      type="checkbox"
                      defaultChecked
                    ></input>
                  ) : (
                    <input
                      className="w-4 h-4 rounded-none"
                      type="checkbox"
                    ></input>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
