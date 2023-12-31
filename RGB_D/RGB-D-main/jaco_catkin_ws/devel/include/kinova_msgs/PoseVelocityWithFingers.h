// Generated by gencpp from file kinova_msgs/PoseVelocityWithFingers.msg
// DO NOT EDIT!


#ifndef KINOVA_MSGS_MESSAGE_POSEVELOCITYWITHFINGERS_H
#define KINOVA_MSGS_MESSAGE_POSEVELOCITYWITHFINGERS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace kinova_msgs
{
template <class ContainerAllocator>
struct PoseVelocityWithFingers_
{
  typedef PoseVelocityWithFingers_<ContainerAllocator> Type;

  PoseVelocityWithFingers_()
    : twist_linear_x(0.0)
    , twist_linear_y(0.0)
    , twist_linear_z(0.0)
    , twist_angular_x(0.0)
    , twist_angular_y(0.0)
    , twist_angular_z(0.0)
    , fingers_closure_percentage(0.0)  {
    }
  PoseVelocityWithFingers_(const ContainerAllocator& _alloc)
    : twist_linear_x(0.0)
    , twist_linear_y(0.0)
    , twist_linear_z(0.0)
    , twist_angular_x(0.0)
    , twist_angular_y(0.0)
    , twist_angular_z(0.0)
    , fingers_closure_percentage(0.0)  {
  (void)_alloc;
    }



   typedef float _twist_linear_x_type;
  _twist_linear_x_type twist_linear_x;

   typedef float _twist_linear_y_type;
  _twist_linear_y_type twist_linear_y;

   typedef float _twist_linear_z_type;
  _twist_linear_z_type twist_linear_z;

   typedef float _twist_angular_x_type;
  _twist_angular_x_type twist_angular_x;

   typedef float _twist_angular_y_type;
  _twist_angular_y_type twist_angular_y;

   typedef float _twist_angular_z_type;
  _twist_angular_z_type twist_angular_z;

   typedef float _fingers_closure_percentage_type;
  _fingers_closure_percentage_type fingers_closure_percentage;





  typedef boost::shared_ptr< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> const> ConstPtr;

}; // struct PoseVelocityWithFingers_

typedef ::kinova_msgs::PoseVelocityWithFingers_<std::allocator<void> > PoseVelocityWithFingers;

typedef boost::shared_ptr< ::kinova_msgs::PoseVelocityWithFingers > PoseVelocityWithFingersPtr;
typedef boost::shared_ptr< ::kinova_msgs::PoseVelocityWithFingers const> PoseVelocityWithFingersConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator1> & lhs, const ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator2> & rhs)
{
  return lhs.twist_linear_x == rhs.twist_linear_x &&
    lhs.twist_linear_y == rhs.twist_linear_y &&
    lhs.twist_linear_z == rhs.twist_linear_z &&
    lhs.twist_angular_x == rhs.twist_angular_x &&
    lhs.twist_angular_y == rhs.twist_angular_y &&
    lhs.twist_angular_z == rhs.twist_angular_z &&
    lhs.fingers_closure_percentage == rhs.fingers_closure_percentage;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator1> & lhs, const ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace kinova_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2788ab35d01df923e0e72d7c730c2511";
  }

  static const char* value(const ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2788ab35d01df923ULL;
  static const uint64_t static_value2 = 0xe0e72d7c730c2511ULL;
};

template<class ContainerAllocator>
struct DataType< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> >
{
  static const char* value()
  {
    return "kinova_msgs/PoseVelocityWithFingers";
  }

  static const char* value(const ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 twist_linear_x\n"
"float32 twist_linear_y\n"
"float32 twist_linear_z\n"
"float32 twist_angular_x\n"
"float32 twist_angular_y\n"
"float32 twist_angular_z\n"
"float32 fingers_closure_percentage\n"
;
  }

  static const char* value(const ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.twist_linear_x);
      stream.next(m.twist_linear_y);
      stream.next(m.twist_linear_z);
      stream.next(m.twist_angular_x);
      stream.next(m.twist_angular_y);
      stream.next(m.twist_angular_z);
      stream.next(m.fingers_closure_percentage);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PoseVelocityWithFingers_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::kinova_msgs::PoseVelocityWithFingers_<ContainerAllocator>& v)
  {
    s << indent << "twist_linear_x: ";
    Printer<float>::stream(s, indent + "  ", v.twist_linear_x);
    s << indent << "twist_linear_y: ";
    Printer<float>::stream(s, indent + "  ", v.twist_linear_y);
    s << indent << "twist_linear_z: ";
    Printer<float>::stream(s, indent + "  ", v.twist_linear_z);
    s << indent << "twist_angular_x: ";
    Printer<float>::stream(s, indent + "  ", v.twist_angular_x);
    s << indent << "twist_angular_y: ";
    Printer<float>::stream(s, indent + "  ", v.twist_angular_y);
    s << indent << "twist_angular_z: ";
    Printer<float>::stream(s, indent + "  ", v.twist_angular_z);
    s << indent << "fingers_closure_percentage: ";
    Printer<float>::stream(s, indent + "  ", v.fingers_closure_percentage);
  }
};

} // namespace message_operations
} // namespace ros

#endif // KINOVA_MSGS_MESSAGE_POSEVELOCITYWITHFINGERS_H
