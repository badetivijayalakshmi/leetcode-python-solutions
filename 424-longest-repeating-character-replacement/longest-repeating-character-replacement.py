class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency array for 26 uppercase English letters
        freq = [0] * 26         
        left, max_freq, max_window = 0, 0, 0

        for right in range(len(s)):
            # Update frequency of the current character
            idx = ord(s[right]) - ord('A')
            freq[idx] += 1
            
            # Keep track of the most frequent character in the current window
            max_freq = max(max_freq, freq[idx])

            # Current window size: (right - left + 1)
            # Check if replacements needed exceed k
            if (right - left + 1) - max_freq > k:
                # Shrink window from the left
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            # Update the global maximum window size
            max_window = max(max_window, right - left + 1)

        return max_window