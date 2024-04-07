import 'package:flutter/material.dart';
import 'package:speed_test_dart/classes/classes.dart';
import 'package:speed_test_dart/speed_test_dart.dart';
import 'package:syncfusion_flutter_gauges/gauges.dart';

void main() => runApp(const MyApp());

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  SpeedTestDart tester = SpeedTestDart();
  List<Server> bestServersList = [];

  double downloadRate = 0;
  double uploadRate = 0;
  double _speedValue = 0;

  bool readyToTest = false;
  bool loadingDownload = false;
  bool loadingUpload = false;

  Future<void> setBestServers() async {
      final settings = await tester.getSettings();
      final servers = settings.servers;

      final _bestServersList = await tester.getBestServers(
        servers: servers,
      );

      setState(() {
        bestServersList = _bestServersList;
        readyToTest = true;
      });
    }

  Future<void> _testDownloadSpeed() async {
      setState(() {
        loadingDownload = true;
      });
      final _downloadRate =
          await tester.testDownloadSpeed(servers: bestServersList);
      setState(() {
        downloadRate = _downloadRate;
        _speedValue = downloadRate;
        loadingDownload = false;
      });
    } 

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(primarySwatch: Colors.green),
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Gfg Internet Speed Tester'),
        ),
        body: SingleChildScrollView(
          child: Center(child: Text("Basic UI")),
        ),
      ),
    );
  }
}
