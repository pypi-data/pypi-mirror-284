# Convolog

A small package used for creating conversation logs

> Started conversation at 2024-07-10 18:38:33
2024-07-10 18:38:33 [Alice]: Hello, how are you?
2024-07-10 18:38:33 [Bob]: I'm doing well, thank you!

## Basic Usage

**Installation**

> pip install convolog

**Template Code**

    from convolog import Conversation
    import  time
    if __name__ == '__main__':
	    convo = Conversation("session1")
	    convo.add_log("Alice", "Hello, how are you?")
	    convo.add_log("Bob", "I'm doing well, thank you!")
	    time.sleep(5)
	    convo.delete_conversation()

I dont want to create a documentation for this so here's the entire documentation:

## Conversation Class
|Function|Description |
|--|--|
|Conversation(identifier: str, file_path: str = None)  | Creates a conversation (will automatically create a file)  |
|get_read_file()  | Returns the file with read permissions  |
|get_write_file()  | Returns the file with write permissions  |
|add_log(source: str, message: str)  | Adds a conversation log  |
|delete_conversation()  | Deletes the conversation file (may be dangerous idk) |