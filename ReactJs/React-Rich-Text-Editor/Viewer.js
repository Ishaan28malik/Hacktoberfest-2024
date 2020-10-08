import React, { Component } from "react";
import classes from "./ContentViewer.module.css";
import { Editor } from "react-draft-wysiwyg";
import {
  EditorState,
  convertToRaw,
  ContentState,
  convertFromRaw,
} from "draft-js";
import { caseStudies } from "../../Data/Data";

let title, image;
class CaseStudy extends Component {
  constructor(props) {
    super(props);
    this.state = {};
    this.state.editorState = EditorState.createEmpty();
  }

  state = {};

  componentDidMount() {
    this.getArticle();
  }

  componentDidUpdate(prevProps) {
    if (this.props.match.params.caseStudy != prevProps.match.params.caseStudy) {
      this.getArticle();
    }
  }

  getArticle = () => {
    window.scrollTo(0, 0);
    console.log(caseStudies);
    let name = this.props.match.params.caseStudy;
    title = this.props.match.params.caseStudy;
    image = caseStudies[name].imageUrl;
    let content = caseStudies[name];
    if (content != null) {
      /* Parse the Editor State*/ 
      let conentJson = JSON.parse(content.editorState);
      
      /*Convert from RAW the parsed editor state and Create a new Editor State */ 
      let editorState = EditorState.createWithContent(
        convertFromRaw(JSON.parse(content.editorState))
      );
      console.log(process.env.REACT_APP_CDN_BUCKET);
      console.log(content);
      this.setState({
        ...this.state,
        editorState,
      });
    }
  };

  render() {
    return (
      <>
        <div className={classes.innerPageBanner2}>
          <img src={image} />
          <h1>{title}</h1>
        </div>
        <div className={classes.container + " container"}>
          <div className="text-center"></div>
          <Editor
            toolbarClassName={classes.toolbarClassName}
            editorState={this.state.editorState}
            readOnly={true}
          />
        </div>
      </>
    );
  }
}

export default CaseStudy;