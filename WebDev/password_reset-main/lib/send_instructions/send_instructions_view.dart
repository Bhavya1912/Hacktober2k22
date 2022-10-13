import 'package:flutter/material.dart';

import '../check_email/check_email_view.dart';
import '../util.dart';

class SendInstructionsView extends StatelessWidget {
  const SendInstructionsView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Back',
          style: TextStyle(color: Colors.black),
        ),
        leadingWidth: 30,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () {},
        ),
        actions: const [
          Padding(
            padding: EdgeInsets.only(right: 16.0),
            child: Icon(Icons.help_outline),
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ListView(
          children: [
            Text(
              'Reset Password',
              style: Theme.of(context).textTheme.headline4,
            ),
            const SizedBox(
              height: 16,
            ),
            Text(
              'Enter the email associated with your account and we\'ll send an email with instructions to reset your password',
              style: Theme.of(context).textTheme.subtitle1,
            ),
            const SizedBox(
              height: 16,
            ),
            Text(
              'Email address',
              style: Theme.of(context).textTheme.subtitle1,
            ),
            const SizedBox(
              height: 8,
            ),
            SizedBox(
              height: 50,
              child: TextFormField(
                style:
                const TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
              ),
            ),
            const SizedBox(
              height: 16,
            ),
            Row(
              children: [
                Expanded(
                    child: ElevatedButton(
                      onPressed: () {
                        //navigate to check email view
                        Util.routeToWidget(context, const CheckEmailView());
                      },
                      child: const Text(
                        'Send Instructions',
                        style: TextStyle(fontSize: 20),
                      ),
                    )),
              ],
            )
          ],
        ),
      ),
    );
  }
}