import React from 'react';


class Uploader extends React.Component {

    constructor() {
        super();

        this.handleFileChange = this.handleFileChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

        this.state = {};
    }

    render() {
        return (<div className="text-center">
                    <h2>Upload your music</h2>
                    <div>Upload your favorite song in mp3 format and we'll queue it
                        so you can hear it and watch a customized light show.
                    </div>
                    <div>Happy Holidays!</div>
                    <form onSubmit={this.handleSubmit}>
                        <div className="form-group col-sm-4 col-sm-offset-4">
                            <div className="input-group">
                                <label className="input-group-btn">
                                    <span className="btn btn-default">
                                        Browse… <input type="file" 
                                            name="audio" 
                                            className="hidden" 
                                            accept="audio/*"
                                            onChange={this.handleFileChange} />
                                    </span>
                                </label>
                                <input type="text" 
                                    className="form-control"
                                    value={this.state.audioFile ? this.state.audioFile.name : ""} 
                                    readOnly="" />
                            </div>  
                        </div>
                        <div className="clearfix"></div>
                        <div className="form-group col-sm-4 col-sm-offset-4">                                                             
                            <button type="submit" 
                                className="form-control btn btn-primary"
                                disabled={this.state.isUploading}
                                onClick={this.handleSubmit}>UPLOAD</button>                            
                        </div>
                        <div className="clearfix"></div>
                    </form>
                </div>);
    }

    handleFileChange(e) {
        e.preventDefault();
        
        let audioFile = e.target.files[0];

        this.setState({
            audioFile: audioFile
        });
    }

    handleSubmit(e) {
        e.preventDefault();

        if (!this.state.audioFile) {
            // Warn that no file is selected
            return;
        }

        this.setState({
            isUploading: true
        });

        var data = new FormData()
        data.append('audio', this.state.audioFile)

        fetch('/api/upload', {
                method: 'POST',
                body: data       
            })
            .then(function(r) {
                return r.json();  
            })
            .then(function(response) {
                if (response.state === 'SUCCESS') {
                    // Notify that file is uploaded
                    
                } else {
                    // Notify that file failed to upload
                    
                }
                
            })
            .finally(function() {                
                this.setState({
                    isUploading: false
                });
            })
    }
}

export default Uploader;