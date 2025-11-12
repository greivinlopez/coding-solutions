# ------------------------
# 1410. HTML Entity Parser
# ------------------------

# Problem: https://leetcode.com/problems/html-entity-parser
#
# HTML entity parser is the parser that takes HTML code as input and replace all
# the entities of the special characters by the characters itself.
# 
# The special characters and their entities for HTML are:
# 
#   * Quotation Mark: the entity is &quot; and symbol character is ".
#   * Single Quote Mark: the entity is &apos; and symbol character is '.
#   * Ampersand: the entity is &amp; and symbol character is &.
#   * Greater Than Sign: the entity is &gt; and symbol character is >.
#   * Less Than Sign: the entity is &lt; and symbol character is <.
#   * Slash: the entity is &frasl; and symbol character is /.
# 
# Given the input text string to the HTML parser, you have to implement the entity
# parser.
# 
# Return the text after replacing the entities by the special characters.
# 
# Example 1:
# 
# Input: text = "&amp; is an HTML entity but &ambassador; is not."
# Output: "& is an HTML entity but &ambassador; is not."
# 
# Explanation: The parser will replace the &amp; entity by &
# 
# Example 2:
# 
# Input: text = "and I quote: &quot;...&quot;"
# Output: "and I quote: \"...\""
# 
# 
# Constraints:
#   1 <= text.length <= 10⁵
#   The string may contain any possible characters out of all the 256 ASCII characters.


# Solution: https://algo.monster/liteproblems/1410
# Credit: AlgoMonster
def entity_parser(text):
    # Dictionary mapping HTML entities to their corresponding characters
    entity_map = {
        '&quot;': '"',
        '&apos;': "'",
        '&amp;': "&",
        "&gt;": '>',
        "&lt;": '<',
        "&frasl;": '/',
    }
    
    # Initialize position index and get text length
    position = 0
    text_length = len(text)
    result = []
    
    # Process each character in the text
    while position < text_length:
        # Try to match entities of different lengths (1 to 7 characters)
        # The longest entity is "&frasl;" which is 7 characters
        entity_found = False
        
        for entity_length in range(1, 8):
            end_position = position + entity_length
            potential_entity = text[position:end_position]
            
            # Check if the substring matches any HTML entity
            if potential_entity in entity_map:
                # Replace entity with its corresponding character
                result.append(entity_map[potential_entity])
                position = end_position
                entity_found = True
                break
        
        # If no entity was found, append the current character as-is
        if not entity_found:
            result.append(text[position])
            position += 1
    
    # Join all characters to form the final string
    return ''.join(result)
    # Time: O(n) -> O(n * l) l is the maximum length of an HTML entity (which is 7 for "&frasl;").
    # Space: O(n)


def main():
    result = entity_parser(text = "&amp; is an HTML entity but &ambassador; is not.")
    print(result) # "& is an HTML entity but &ambassador; is not."

    result = entity_parser(text = "and I quote: &quot;...&quot;")
    print(result) # "and I quote: "...""

if __name__ == "__main__":
    main()
