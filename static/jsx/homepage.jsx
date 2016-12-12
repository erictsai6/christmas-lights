import React from 'react';

import Uploader from './components/uploader.jsx';
import Queue from './components/queue.jsx';

class Homepage extends React.Component {

    render() {
        return (<div className="row">
                    <Uploader className="col-xs-12"></Uploader>
                    <Queue className="col-xs-12"></Queue>
                </div>);
    }
}

export default Homepage;