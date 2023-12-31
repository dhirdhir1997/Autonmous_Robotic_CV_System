// Generated by gencpp from file kinova_msgs/JointVelocity.msg
// DO NOT EDIT!


#ifndef KINOVA_MSGS_MESSAGE_JOINTVELOCITY_H
#define KINOVA_MSGS_MESSAGE_JOINTVELOCITY_H


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
struct JointVelocity_
{
  typedef JointVelocity_<ContainerAllocator> Type;

  JointVelocity_()
    : joint1(0.0)
    , joint2(0.0)
    , joint3(0.0)
    , joint4(0.0)
    , joint5(0.0)
    , joint6(0.0)
    , joint7(0.0)  {
    }
  JointVelocity_(const ContainerAllocator& _alloc)
    : joint1(0.0)
    , joint2(0.0)
    , joint3(0.0)
    , joint4(0.0)
    , joint5(0.0)
    , joint6(0.0)
    , joint7(0.0)  {
  (void)_alloc;
    }



   typedef float _joint1_type;
  _joint1_type joint1;

   typedef float _joint2_type;
  _joint2_type joint2;

   typedef float _joint3_type;
  _joint3_type joint3;

   typedef float _joint4_type;
  _joint4_type joint4;

   typedef float _joint5_type;
  _joint5_type joint5;

   typedef float _joint6_type;
  _joint6_type joint6;

   typedef float _joint7_type;
  _joint7_type joint7;





  typedef boost::shared_ptr< ::kinova_msgs::JointVelocity_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::kinova_msgs::JointVelocity_<ContainerAllocator> const> ConstPtr;

}; // struct JointVelocity_

typedef ::kinova_msgs::JointVelocity_<std::allocator<void> > JointVelocity;

typedef boost::shared_ptr< ::kinova_msgs::JointVelocity > JointVelocityPtr;
typedef boost::shared_ptr< ::kinova_msgs::JointVelocity const> JointVelocityConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::kinova_msgs::JointVelocity_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::kinova_msgs::JointVelocity_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::kinova_msgs::JointVelocity_<ContainerAllocator1> & lhs, const ::kinova_msgs::JointVelocity_<ContainerAllocator2> & rhs)
{
  return lhs.joint1 == rhs.joint1 &&
    lhs.joint2 == rhs.joint2 &&
    lhs.joint3 == rhs.joint3 &&
    lhs.joint4 == rhs.joint4 &&
    lhs.joint5 == rhs.joint5 &&
    lhs.joint6 == rhs.joint6 &&
    lhs.joint7 == rhs.joint7;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::kinova_msgs::JointVelocity_<ContainerAllocator1> & lhs, const ::kinova_msgs::JointVelocity_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace kinova_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::kinova_msgs::JointVelocity_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::kinova_msgs::JointVelocity_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinova_msgs::JointVelocity_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinova_msgs::JointVelocity_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinova_msgs::JointVelocity_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinova_msgs::JointVelocity_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::kinova_msgs::JointVelocity_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bf16c4e5154848a0767d1aaab0a4796b";
  }

  static const char* value(const ::kinova_msgs::JointVelocity_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbf16c4e5154848a0ULL;
  static const uint64_t static_value2 = 0x767d1aaab0a4796bULL;
};

template<class ContainerAllocator>
struct DataType< ::kinova_msgs::JointVelocity_<ContainerAllocator> >
{
  static const char* value()
  {
    return "kinova_msgs/JointVelocity";
  }

  static const char* value(const ::kinova_msgs::JointVelocity_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::kinova_msgs::JointVelocity_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 joint1\n"
"float32 joint2\n"
"float32 joint3\n"
"float32 joint4\n"
"float32 joint5\n"
"float32 joint6\n"
"float32 joint7\n"
;
  }

  static const char* value(const ::kinova_msgs::JointVelocity_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::kinova_msgs::JointVelocity_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.joint1);
      stream.next(m.joint2);
      stream.next(m.joint3);
      stream.next(m.joint4);
      stream.next(m.joint5);
      stream.next(m.joint6);
      stream.next(m.joint7);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct JointVelocity_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::kinova_msgs::JointVelocity_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::kinova_msgs::JointVelocity_<ContainerAllocator>& v)
  {
    s << indent << "joint1: ";
    Printer<float>::stream(s, indent + "  ", v.joint1);
    s << indent << "joint2: ";
    Printer<float>::stream(s, indent + "  ", v.joint2);
    s << indent << "joint3: ";
    Printer<float>::stream(s, indent + "  ", v.joint3);
    s << indent << "joint4: ";
    Printer<float>::stream(s, indent + "  ", v.joint4);
    s << indent << "joint5: ";
    Printer<float>::stream(s, indent + "  ", v.joint5);
    s << indent << "joint6: ";
    Printer<float>::stream(s, indent + "  ", v.joint6);
    s << indent << "joint7: ";
    Printer<float>::stream(s, indent + "  ", v.joint7);
  }
};

} // namespace message_operations
} // namespace ros

#endif // KINOVA_MSGS_MESSAGE_JOINTVELOCITY_H
