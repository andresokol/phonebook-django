"use strict";

const Task = ({ task }) => {
  return (
    <div className="item">
      <div className="ui checkbox">
        <input type="checkbox" checked={task.is_done} onChange={() => {}} />
        <label>{task.title}</label>
      </div>
    </div>
  );
};

const TaskInput = ({ createTask }) => {
  const [value, setValue] = React.useState("");

  const onButtonClick = () => {
    createTask(value).then(() => setValue(""));
  };

  return (
    <div className="ui action input">
      <input
        type="text"
        placeholder="New task..."
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
      <button className="ui button green" onClick={onButtonClick}>
        Add
      </button>
    </div>
  );
};

const Container = () => {
  const [loading, setLoading] = React.useState(true);
  const [tasks, setTasks] = React.useState([]);

  React.useEffect(() => {
    //...
  }, []);

  const createTask = async (newTaskTitle) => {
    // ...
  };

  if (loading) {
    return (
      <div className="ui active inverted dimmer">
        <div className="ui loader"></div>
      </div>
    );
  }

  return (
    <div className="ui very padded text container" style={{ paddingTop: 50 }}>
      <h1 className="ui header">Hello, world!</h1>
      <div className="ui list">
        {tasks.map((task) => (
          <Task task={task} key />
        ))}
      </div>
      <TaskInput createTask={createTask} />
    </div>
  );
};

const domContainer = document.querySelector("#app");
const root = ReactDOM.createRoot(domContainer);
root.render(<Container />);
