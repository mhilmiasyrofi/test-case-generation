//
//  main.swift
//  tts
//
//  Created by Muhammad Hilmi Asyrofi on 21/1/20.
//  Copyright © 2020 Muhammad Hilmi Asyrofi. All rights reserved.
//
//  Text-to-Speech on OSX

import Foundation
import AppKit

let bash: CommandExecuting = Bash()


// show the installed voice list with major attributes
//let voices = NSSpeechSynthesizer.availableVoices.map { v in (v, NSSpeechSynthesizer.attributes(forVoice: v)[NSSpeechSynthesizer.VoiceAttributeKey.localeIdentifier] as! String) }.sorted  { ($0.1, $0.0.rawValue) < ($1.1, $1.0.rawValue) }
//for (k, v) in voices {
//    if (v.contains("en")) {
//        print( "\(k) speaks \(v)" )
//    }
//}

//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.fiona) speaks en-scotland
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.karen) speaks en_AU
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.daniel) speaks en_GB
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.moira) speaks en_IE
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.rishi) speaks en_IN
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.veena) speaks en_IN
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.Alex) speaks en_US
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.Fred) speaks en_US
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.Victoria) speaks en_US
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.samantha) speaks en_US
//NSSpeechSynthesizerVoiceName(_rawValue: com.apple.speech.synthesis.voice.tessa) speaks en_ZA

//let synth = NSSpeechSynthesizer()
//synth.setVoice(NSSpeechSynthesizer.VoiceName(rawValue: "com.apple.speech.synthesis.voice.Alex"))
//let url = Foundation.URL.init(fileURLWithPath: "/Users/mhilmiasyrofi/Documents/tts/test.aiff")
//synth.startSpeaking("Alexa open transcribe test", to: url)

// File path (change this).
let path = "/Users/mhilmiasyrofi/Documents/tts/tts/alexa-test-command.txt"

// Read an entire text file into an NSString.
let contents = try NSString(contentsOfFile: path,
    encoding: String.Encoding.ascii.rawValue)


// Process each lines
var i = 0
let synth = NSSpeechSynthesizer()
synth.setVoice(NSSpeechSynthesizer.VoiceName(rawValue: "com.apple.speech.synthesis.voice.moira"))
contents.enumerateLines({ (line, stop) -> () in
    i = i + 1
//    let output_file =  String(format:"/Users/mhilmiasyrofi/Documents/tts/tts/generated_data/audio_%02d.aiff", i)
    let output_file =  String(format:"/Users/mhilmiasyrofi/Documents/deepspeech/aiff_data/audio_%02d.aiff", i)
    
    let url = Foundation.URL.init(fileURLWithPath: output_file)
//    let skill_executor = "Alexa ask transcribe test to record this "
    let skill_executor = ""
    let skill_command = line
    let command = skill_executor + skill_command
    synth.startSpeaking(command, to: url)
    print("Generated: " + command)
    if let lsOutput = bash.execute(commandName: "ffmpeg", arguments: ["-i", String(format:"/Users/mhilmiasyrofi/Documents/deepspeech/aiff_data/audio_%02d.aiff", i), "-acodec", "pcm_s16le", "-ac", "1" , "-ar", "16000", String(format: "/Users/mhilmiasyrofi/Documents/deepspeech/data/audio_%02d.wav", i), "-y"]) { print("Convert the audio format\n")}
})



