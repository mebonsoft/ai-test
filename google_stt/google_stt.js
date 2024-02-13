// 라이브러리 import
const {SpeechClient} = require('@google-cloud/speech');

// 서비스 계정 키 정보 설정
const projectId = 'YOUR_PROJECT_ID';
const keyFilename = 'PATH_TO_YOUR_KEY_FILE.json';

// Speech-to-Text 클라이언트 생성
const speechClient = new SpeechClient({
  projectId,
  keyFilename,
});

// 요청 설정
const request = {
  config: {
    encoding: 'RAW',
    languageCode: 'ko-KR',
    sampleRateHertz: 16000,
  },
  interimResults: true,
};

// 음성 스트림 생성
const recognizeStream = speechClient.recognizeStream(request);

// 마이크 스트림 설정
const mic = require('mic');

const micStream = mic({
  rate: 16000,
  channels: 1,
  bitDepth: 16,
  format: 'raw',
});

// 마이크 스트림을 Speech-to-Text API로 전송
micStream.pipe(recognizeStream);

// 음성 인식 결과 처리
recognizeStream.on('data', (data) => {
  // 결과 출력
  const transcription = data.results[0].alternatives[0].transcript;
  console.log('음성 인식 결과:', transcription);
});

// 오류 처리
recognizeStream.on('error', (err) => {
  console.error('오류 발생:', err);
});

// 스트림 종료
micStream.on('end', () => {
  console.log('마이크 스트림 종료');
});

// 프로그램 종료 시 스트림 종료
process.on('SIGINT', () => {
  micStream.end();
  recognizeStream.end();
});
