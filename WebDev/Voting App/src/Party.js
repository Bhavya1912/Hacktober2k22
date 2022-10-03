import React, { useEffect, useState } from "react";
import {
  Button,
  Card,
  CardContent,
  CardMedia,
  Typography,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
} from "@mui/material";
import "./Party.css";
import db from "./firebase";
function Party({ name, image, voted, func, userName }) {
  const [vote, setVote] = useState(false);
  const [open, setOpen] = useState(false);

  const addNameToDB = (name) => {
    if (name !== "" && name !== null) {
      db.collection("names").add({
        name: name,
      });
    }
  };

  const voteSubmit = (event) => {
    event.preventDefault();
    setOpen(false);
    setVote(true);
    func(true);
    addNameToDB(userName);
  };

  const handleClickOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  useEffect(() => {
    if (vote === true) {
    }
  }, [vote]);

  return (
    <div className="party">
      <Card className="party__card" sx={{ maxWidth: 200 }}>
        <CardContent className="party__cardContent1">
          <Typography variant="h5">
            <strong> {name} </strong>
          </Typography>
        </CardContent>
        <CardMedia
          className="party__image"
          component="img"
          image={image}
        ></CardMedia>
        <CardContent>
          <center>
            <Button
              className="party__voteBtn"
              variant="contained"
              color="success"
              onClick={handleClickOpen}
              disabled={voted}
            >
              Vote
            </Button>
          </center>
        </CardContent>
      </Card>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">
          {`Are you sure that you want to vote for ${name}?`}
        </DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            If you wish to go back and change your decision then click on{" "}
            <i>Disagree</i>, otherwise click on <i>Agree</i>.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Disagree</Button>
          <Button onClick={voteSubmit} autoFocus>
            Agree
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}

export default Party;
