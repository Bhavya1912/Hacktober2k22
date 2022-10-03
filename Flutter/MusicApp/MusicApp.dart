import 'package:flutter/material.dart';

void main(){
  runApp(const MyApp());
 // runApp(const SideBar());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Music Albums';



    return MaterialApp(
      debugShowCheckedModeBanner: false,

      title: title,
      home: Scaffold(
        drawer: Drawer(
          child: ListView(
          padding: EdgeInsets.zero,
          children: [
            const DrawerHeader(
              decoration: BoxDecoration(color: Colors.blueGrey,
              ),
              child: Text('Artists', textScaleFactor: 3, textAlign: TextAlign.center,),
            ),
            ListTile(
              title: const Text('Nirvana'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            ListTile(
              title: const Text('The Strokes'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            ListTile(
              title: const Text('Weezer'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            ListTile(
              title: const Text('Greenday'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
          ],
        ),
        ),
        appBar: AppBar(
          title: const Text(title),
          backgroundColor: const Color(0xDD000000),
        ),
        body: GridView.count(
          crossAxisCount: 2,
          children: [
            Card(
              child: Image.network('https://upload.wikimedia.org/wikipedia/en/b/b7/NirvanaNevermindalbumcover.jpg'),
    ),
            Card(
              child: Image.network('https://i.scdn.co/image/ab67616d0000b27387096355b706ccb439f7a689'),
            ),
            Card(
              child: Image.network('https://media.pitchfork.com/photos/5931bf169726246adc7c3c41/master/w_658,h_658,c_limit/b55f98f3.jpg'),
    ),
    Card(
      child: Image.network('https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/Nirvana-Bleach.jpg/220px-Nirvana-Bleach.jpg'),
    ),
    Card(
      child: Image.network('https://upload.wikimedia.org/wikipedia/en/8/85/Nirvana-Incesticide.jpg'),
    ),
            Card(
              child: Image.network('https://upload.wikimedia.org/wikipedia/en/e/ed/Green_Day_-_American_Idiot_album_cover.png'),
            ),
            Card(
              child: Image.network('https://m.media-amazon.com/images/I/91L+jT5HY7L._SL1500_.jpg'),
            ),
            Card(
              child: Image.network('https://upload.wikimedia.org/wikipedia/en/b/b0/Green_Day_-_Uno%21_cover.jpg'),
            ),
            Card(
              child: Image.network('https://i.pinimg.com/736x/93/65/aa/9365aa989a162178a9709d96f5eff372.jpg'),
            ),
            Card(
              child: Image.network('https://i.scdn.co/image/ab67616d0000b273f07ef193e0bb6a238ea37f0a'),
            ),
            Card(
              child: Image.network('https://m.media-amazon.com/images/I/71nYpz++VCL._SL1400_.jpg'),
            ),
            Card(
              child: Image.network('https://m.media-amazon.com/images/I/61pAyFJQ43L._SL1400_.jpg'),
            ),
            ],
            ),
          ),
        );

  }
}
