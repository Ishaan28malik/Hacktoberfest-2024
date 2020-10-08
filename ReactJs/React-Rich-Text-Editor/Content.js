import React, { Component } from "react"
import classes from "./ContentGenerator.module.css"
import { EditorState, convertToRaw, ContentState, convertFromRaw } from 'draft-js';
import { Editor } from 'react-draft-wysiwyg';
import 'react-draft-wysiwyg/dist/react-draft-wysiwyg.css';

class Content extends Component {
    constructor(props) {
        super(props);
        this.state = {}

        const content = window.localStorage.getItem('content');

        if (content) {
            this.state.editorState = EditorState.createWithContent(convertFromRaw(JSON.parse(content)));
        } else {
            this.state.editorState = EditorState.createEmpty();
        }
    }
    state = {
        contentState: null
    }

    onEditorStateChange = (editorState) => {
        const contentState = editorState.getCurrentContent();
        this.saveContent(contentState);
        this.setState({
            editorState,
        });
    }

    saveContent = (content) => {
        window.localStorage.setItem('content', JSON.stringify(convertToRaw(content)));
    }


    render() {

        const { editorState } = this.state;

        return (
            <div className={classes.container + " container"}>
                <Editor
                    editorState={editorState}
                    wrapperClassName={classes.editorWrapper}
                    editorClassName="demo-editor"
                    onEditorStateChange={this.onEditorStateChange}
                />
            {/* Now what ever article you type in above, the strigified value will be shown in the text input below. You can either manually append this value to the Data.json file or most probably
                make a request to the backend to store this editor state.
            */}    
            <input type="text" value={JSON.stringify(JSON.stringify(convertToRaw(editorState.getCurrentContent())))} />
            </div>
        )
    }
}

export default Content