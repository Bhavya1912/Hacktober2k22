import React, { useEffect, useState } from "react";
import "./App.css";
import Party from "./Party";
import db from "./firebase";

function App() {
  const [name, setName] = useState("");
  const [voted, setVoted] = useState(false);

  const pullData = (data) => {
    setVoted(data);
  };

  useEffect(() => {
    setName(prompt("Enter your name: "));
    db.collection("names")
      .get()
      .then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
          if (name === doc.data().name) {
            setVoted(true);
          }
          console.log(doc.data().name);
        });
      });
  }, [name]);

  return (
    <div className="app">
      <div className="app__header">
        <div className="app__header__title">
          <h2>भारतीय चुनाव मतदाता पोर्टल</h2>
          <h3>
            <i>Vote, it’s your Right and Responsibility</i>
          </h3>
        </div>

        {/* <img
          className="app__header__img"
          src="https://img.freepik.com/free-vector/india-vote-concept-design-with-flag_1017-17778.jpg?w=740&t=st=1662199448~exp=1662200048~hmac=8a527734f97e24ee00ff84b0546a18f110906a6e3d8298ade9a973fe7c2139ac"
          alt=""
        /> */}
      </div>
      <div className="app__container">
        <div className="app__containerTitles">
          {voted ? (
            <>
              <h1 className="app__containerT1">
                Your vote has been submitted sucessfully.
              </h1>
              <h2 className="app__containerT2">Thank you, {name}</h2>
            </>
          ) : (
            <>
              <h1 className="app__containerT1">
                Have a vision? Make a right decision! VOTE!
              </h1>
              <h2 className="app__containerT2">Welcome, {name}</h2>
            </>
          )}
        </div>
        <div className="app__containerParties">
          <div className="appcontainerPartiesEachParty">
            <Party
              name="BJP"
              image="https://upload.wikimedia.org/wikipedia/commons/a/ad/Bjp.png"
              voted={voted}
              func={pullData}
              userName={name}
            />
          </div>
          <div className="appcontainerPartiesEachParty">
            <Party
              name="INC"
              image="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Indian_National_Congress_hand_logo.png/600px-Indian_National_Congress_hand_logo.png"
              voted={voted}
              func={pullData}
              userName={name}
            />
          </div>
          <div className="appcontainerPartiesEachParty">
            <Party
              name="AAP"
              image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_HHTtUUXaPLoaGQXI6zr6D_LmbHLZY2swO2NtepO0pKusnzU7gJ67s2LfFVHBr3Be27k&usqp=CAU"
              voted={voted}
              func={pullData}
              userName={name}
            />
          </div>
          <div className="appcontainerPartiesEachParty">
            <Party
              name="NOTA"
              image="https://cdn.discordapp.com/attachments/938687139397373963/1015920567083352217/Untitled-2.png"
              voted={voted}
              func={pullData}
              userName={name}
            />
          </div>
        </div>
      </div>

      <p className="app__footer">Website by Sarthak Keswani</p>
    </div>
  );
}

export default App;
