import rospy
import rospkg
import tf
import geometry_msgs.msg

class AutonomousVehicleControlROS:
    def __init__(self):
        rospy.init_node('autonomous_vehicle_control')
        self.rospack = rospkg.RosPack()
        self.base_frame = 'base_link'
        self.odom_frame = 'odom'
        self.twist_topic = 'cmd_vel'
        self.linear_velocity = 0.5
        self.angular_velocity = 0.0
        self.twist_publisher = rospy.Publisher(self.twist_topic, geometry_msgs.Twist, queue_size=10)
        self.odom_subscriber = rospy.Subscriber('/odom', geometry_msgs.Odometry, self.odom_callback)
        self.tf_listener = tf.TransformListener()

    def odom_callback(self, odom_msg):
        try:
            (trans, rot) = self.tf_listener.lookupTransform(self.base_frame, self.odom_frame, rospy.Time())
            self.linear_velocity = odom_msg.twist.twist.linear.x
            self.angular_velocity = odom_msg.twist.twist.angular.z
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            pass

    def drive(self, speed, steering_angle):
        twist_msg = geometry_msgs.Twist()
        twist_msg.linear.x = speed
        twist_msg.angular.z = steering_angle
        self.twist_publisher.publish(twist_msg)
