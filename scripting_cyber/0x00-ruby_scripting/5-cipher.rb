#!/usr/bin/env ruby

# CaesarCipher - Implements Caesar Cipher encryption and decryption
class CaesarCipher
  def initialize(shift)
    @shift = shift
  end

  def encrypt(message)
    cipher(message, @shift)
  end

  def decrypt(message)
    cipher(message, -@shift)
  end

  private

  # cipher - Core logic for shifting characters in a message
  # @message: The input string to encrypt or decrypt
  # @shift: Integer value to shift by (positive for encrypt, negative for decrypt)
  def cipher(message, shift)
    message.chars.map do |char|
      if char.match?(/[A-Za-z]/)
        base = char.ord < 91 ? 'A'.ord : 'a'.ord
        (((char.ord - base + shift) % 26) + base).chr
      else
        char
      end
    end.join
  end
end
