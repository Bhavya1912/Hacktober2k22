import firebase from 'firebase/compat/app';
import 'firebase/compat/firestore';


const firebaseApp = firebase.initializeApp({
    apiKey: "AIzaSyALIoBgfepXal0s0-La8OjhVIPj-nZtjrA",
    authDomain: "voting-app-f4327.firebaseapp.com",
    projectId: "voting-app-f4327",
    storageBucket: "voting-app-f4327.appspot.com",
    messagingSenderId: "222516595155",
    appId: "1:222516595155:web:a57737d4e3709580bc4726",
    measurementId: "G-8JDX6YWD52"
  });

const db = firebaseApp.firestore();

export default db;