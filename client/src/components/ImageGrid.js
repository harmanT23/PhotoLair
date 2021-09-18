import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import SizeMe from 'react-sizeme';
import StackGrid from 'react-stack-grid';
import Box from '@material-ui/core/Box';
import CssBaseline from '@material-ui/core/CssBaseline';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardActions from '@material-ui/core/CardActions';
import Typography from '@material-ui/core/Typography';

import * as actions from '../actions';
import BuyAndDownloadImage from '../services/buyAndDownloadImage';
import { checkEmpty }  from '../utilities/checkEmptyObj';


class ImageGrid extends Component {
  componentDidMount() {
    this.props.fetchUser();   
    this.props.fetchImageList();
  }

  getImageList() {
    const imageList = this.props.imageList;
    console.log(imageList)

    if (!checkEmpty(imageList)) {
      return imageList.map((image, idx) => (
        <div 
         key={idx}
        >
         <figure
           style = {{ margin: 10 }}
         >
           <Card>
           <CardHeader
            title={image.image_name}
            titleTypographyProps={{
              variant:'h6', 
              fontSize:'fontSize', 
              fontWeight:'fontWeightLight',
            }}
            style={{ textAlign: 'center' }}
            subheader={'by ' + image.user.username}
           />
             <img 
               onContextMenu={(e) => {
                 e.preventDefault();
               }}
               style={{ width: '100%', height: 'auto', margin: 'auto' }}
               src={image.image}
               alt={'None'}
             />{' '}
             <div
               style={{ padding: '5px' }}
             >
               <CardActions>
                <Typography
                   gutterBottom
                   variant='h6'
                 >
                  <Box
                     style={{ marginRight: '4px' }}
                     fontSize='fontSize'
                     fontWeight='fontWeightLight'
                     m={1}
                   >
                    Credits:
                  </Box>
                 </Typography>
                 <Typography
                   gutterBottom
                   variant='subtitle1'
                   style={{ marginLeft: 0, marginRight: 'auto' }}
                 >
                   <Box
                     fontStyle='normal'
                     fontWeight='fontWeightLight'
                     m={1}
                     style={{ margin: 0 }}
                   >
                    {image.price}
                   </Box>
                 </Typography>
                 <Typography
                   gutterBottom
                   variant='h6'
                 >
                  <Box
                     style={{ marginRight: '4px' }}
                     fontSize='fontSize'
                     fontWeight='fontWeightLight'
                     m={1}
                   >
                    Stock:
                  </Box>
                 </Typography>
                 <Typography
                   gutterBottom
                   variant='subtitle1'
                   style={{ marginLeft: 0, marginRight: 'auto' }}
                 >
                   <Box
                     fontStyle='normal'
                     fontWeight='fontWeightLight'
                     m={1}
                     style={{ margin: 0 }}
                   >
                    {image.inventory}
                   </Box>
                 </Typography>
                 <BuyAndDownloadImage 
                  imageID={image.id}
                  image_name={image.image_name} 
                 />
               </CardActions>
             </div>
           </Card>
         </figure>
        </div>
       ));
    } else {
      return;
    }
  }

  render() {
    const {
      size: { width },
    } = this.props;
    let colWidth = '33.33%';

    if (width <= 768) colWidth = '50%';
    if (width <= 450) colWidth = '80%';

    return(
      <div 
        style={{ width: '80%', margin: 'auto' }}
      >
        <CssBaseline />
        <StackGrid
          monitorImagesLoaded={true}
          columnWidth={colWidth}
        >
          {this.getImageList()}
        </StackGrid>
      </div>
    );
  }
}

function mapStateToProps({ imageList }) {
  return { imageList };
}

export default compose(
  SizeMe(),
  connect(mapStateToProps, actions)
)(ImageGrid);
