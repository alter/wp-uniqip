<?php
/*
Author: ALTER
Author URI: http://www.ag-up.com
Description: wordpress plugin; print UniqIP statistics per day
Plugin name: UniqIP
*/

class UniqIP extends WP_Widget {
	function UniqIP() {
		parent::WP_Widget(false, $name = 'UniqIP');
	}

	function widget($args, $instance) {		
    	extract( $args );
        $title = apply_filters('UniqIP', $instance['title']);
        ?>
              <?php echo $before_widget; ?>
                  <?php if ( $title )
                        echo $before_title . $title . $after_title; ?>
			<?php include("mysql.inc"); ?>
              <?php echo $after_widget; ?>
        <?php
    }

    function update($new_instance, $old_instance) {
        $instance = $old_instance;
        $instance['title'] = strip_tags($new_instance['title']);
        return $instance;
    }


	function form($instance) {
		$title = esc_attr($instance['title']);
		?>
        <p><label for="<?php echo $this->get_field_id('title'); ?>">
			<?php _e('Title:'); ?> <input class="widefat" id="<?php echo $this->get_field_id('title'); ?>" 
			name="<?php echo $this->get_field_name('title'); ?>" type="text" value="<?php echo $title; ?>" /></label>
		</p>
        <?php 
	}
}

add_action('widgets_init', create_function('', 'return register_widget("UniqIP");'));
?>
