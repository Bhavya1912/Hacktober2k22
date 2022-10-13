import 'package:flutter/material.dart';
import 'package:password_reset/send_instructions/send_instructions_view.dart';

// #7b39ed - primary color

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  final MaterialColor primarySwatch = const MaterialColor(0xff7b39ed, <int, Color>{
    50: Color(0xff7b39ed),
    100: Color(0xff7b39ed),
    200: Color(0xff7b39ed),
    300: Color(0xff7b39ed),
    400: Color(0xff7b39ed),
    500: Color(0xff7b39ed),
    600: Color(0xff7b39ed),
    700: Color(0xff7b39ed),
    800: Color(0xff7b39ed),
    900: Color(0xff7b39ed),
  });

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        iconTheme: const IconThemeData(color: Color(0xff7b39ed)),
        inputDecorationTheme: InputDecorationTheme(
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: BorderSide(color: Colors.grey.shade400),
            ),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
            )),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
              minimumSize: const Size(double.infinity, 50),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
              )),
        ),
        textTheme: TextTheme(
            headline4:
            const TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
            subtitle1: TextStyle(
              color: Colors.grey.shade600,
            )),
        appBarTheme: const AppBarTheme(
            backgroundColor: Colors.transparent,
            elevation: 0,
            iconTheme: IconThemeData(color: Colors.black)),
        primaryColor: const Color(0xff7b39ed),
        primarySwatch: primarySwatch,
      ),
      home: const SendInstructionsView(),
    );
  }
}