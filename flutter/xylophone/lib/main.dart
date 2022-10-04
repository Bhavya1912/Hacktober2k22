import 'package:flutter/material.dart';
import 'package:audioplayers/audioplayers.dart';

void main() => runApp(XylophoneApp());

class XylophoneApp extends StatelessWidget {
  void playSound(int sound) {
    final player = AudioCache();
    player.play('note$sound.wav');
  }
  Expanded buildKey( {Color color, int num}){
     return Expanded(
      child: FlatButton(
        color: color,
        onPressed: () {
          playSound(num);
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.black,
        body: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              buildKey(color: Colors.redAccent,num: 1),
              buildKey(color: Colors.green,num: 2),
              buildKey(color: Colors.blue,num: 3),
              buildKey(color: Colors.purple,num: 4),
              buildKey(color: Colors.pink,num: 5),
              buildKey(color: Colors.deepOrange,num: 6),
              buildKey(color: Colors.yellowAccent,num: 7),

            ],
          ),
        ),
      ),
    );
  }
}
