import React from 'react';
import './myApp.css';
import { toast, ToastContainer } from "react-toastify";
import'react-toastify/dist/ReactToastify.css';

class myApp extends React.Component {
  constructor(props) {
    super(props);
    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);

    fetch('http://localhost:5000/myservice/create', {
      method: 'POST',
      body: data,
    }).then((response) => {
      if (response.status === 200){
          toast.success("sucessfully uploaded")
      }
      if (response.status === 400){
        toast.warning("File is Empty")
      }
      if (response.status === 500){
        toast.error("There is some issue with .xlsx file")
      }
    });
  }

  render() {
    return (
      <form onSubmit={this.handleUploadImage}>
        <div className='form'>
          <ToastContainer />
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
          <button>Upload</button>
        </div>
      </form>
    );
  }
}

export default myApp;