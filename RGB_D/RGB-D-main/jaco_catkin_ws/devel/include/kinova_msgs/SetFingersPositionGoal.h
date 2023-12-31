// Generated by gencpp from file kinova_msgs/SetFingersPositionGoal.msg
// DO NOT EDIT!


#ifndef KINOVA_MSGS_MESSAGE_SETFINGERSPOSITIONGOAL_H
#define KINOVA_MSGS_MESSAGE_SETFINGERSPOSITIONGOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <kinova_msgs/FingerPosition.h>

namespace kinova_msgs
{
template <class ContainerAllocator>
struct SetFingersPositionGoal_
{
  typedef SetFingersPositionGoal_<ContainerAllocator> Type;

  SetFingersPositionGoal_()
    : fingers()  {
    }
  SetFingersPositionGoal_(const ContainerAllocator& _alloc)
    : fingers(_alloc)  {
  (void)_alloc;
    }



   typedef  ::kinova_msgs::FingerPosition_<ContainerAllocator>  _fingers_type;
  _fingers_type fingers;





  typedef boost::shared_ptr< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct SetFingersPositionGoal_

typedef ::kinova_msgs::SetFingersPositionGoal_<std::allocator<void> > SetFingersPositionGoal;

typedef boost::shared_ptr< ::kinova_msgs::SetFingersPositionGoal > SetFingersPositionGoalPtr;
typedef boost::shared_ptr< ::kinova_msgs::SetFingersPositionGoal const> SetFingersPositionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator1> & lhs, const ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator2> & rhs)
{
  return lhs.fingers == rhs.fingers;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator1> & lhs, const ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace kinova_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bdbf88b45be6ef8cd65f0b4fc487d49d";
  }

  static const char* value(const ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbdbf88b45be6ef8cULL;
  static const uint64_t static_value2 = 0xd65f0b4fc487d49dULL;
};

template<class ContainerAllocator>
struct DataType< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "kinova_msgs/SetFingersPositionGoal";
  }

  static const char* value(const ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Goal\n"
"FingerPosition fingers\n"
"\n"
"================================================================================\n"
"MSG: kinova_msgs/FingerPosition\n"
"float32 finger1\n"
"float32 finger2\n"
"float32 finger3\n"
;
  }

  static const char* value(const ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.fingers);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetFingersPositionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::kinova_msgs::SetFingersPositionGoal_<ContainerAllocator>& v)
  {
    s << indent << "fingers: ";
    s << std::endl;
    Printer< ::kinova_msgs::FingerPosition_<ContainerAllocator> >::stream(s, indent + "  ", v.fingers);
  }
};

} // namespace message_operations
} // namespace ros

#endif // KINOVA_MSGS_MESSAGE_SETFINGERSPOSITIONGOAL_H
