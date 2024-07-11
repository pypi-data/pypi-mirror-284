#ifndef SUPPORT_INCLUDE_TASK_VISION_OBJECT_DETECTION_TYPES_H_
#define SUPPORT_INCLUDE_TASK_VISION_OBJECT_DETECTION_TYPES_H_

#include <chrono>
#include <limits>  // for numeric_limits<>
#include <string>
#include <type_traits>
#include <vector>

#include "opencv2/opencv.hpp"

template <typename _T1 = float, typename _T2 = float>
static inline void __assert_type() {
  static_assert(
      std::is_pod<_T1>::value && std::is_pod<_T2>::value &&
          std::is_floating_point<_T2>::value &&
          (std::is_integral<_T1>::value || std::is_floating_point<_T1>::value),
      "not support type.");
}  // only support for some specific types. check at compile-time.

// bounding box.
template <typename T1 = float, typename T2 = float>
struct BoundingBoxType {
  typedef T1 value_type;
  typedef T2 score_type;
  value_type x1;
  value_type y1;
  value_type x2;
  value_type y2;
  score_type score;
  const char* label_text;
  unsigned int label;  // for general object detection.
  // convert type.
  template <typename O1, typename O2 = score_type>
  BoundingBoxType<O1, O2> convert_type() const;

  template <typename O1, typename O2 = score_type>
  value_type iou_of(const BoundingBoxType<O1, O2>& other) const;

  value_type width() const;

  value_type height() const;

  value_type area() const;

  cv::Rect rect() const;

  cv::Point2i tl() const;

  cv::Point2i bl() const;

  cv::Point2i rb() const;

  BoundingBoxType()
      : x1(static_cast<value_type>(0)),
        y1(static_cast<value_type>(0)),
        x2(static_cast<value_type>(0)),
        y2(static_cast<value_type>(0)),
        score(static_cast<score_type>(0)),
        label_text(nullptr),
        label(0) {
    __assert_type<value_type, score_type>();
  }
};  // End BoundingBox.

typedef BoundingBoxType<int, float> Boxi;
typedef BoundingBoxType<float, float> Boxf;
typedef BoundingBoxType<double, double> Boxd;

/* implementation for 'BoundingBox'. */
template <typename T1, typename T2>
template <typename O1, typename O2>
inline BoundingBoxType<O1, O2> BoundingBoxType<T1, T2>::convert_type() const {
  typedef O1 other_value_type;
  typedef O2 other_score_type;
  __assert_type<other_value_type, other_score_type>();
  __assert_type<value_type, score_type>();
  BoundingBoxType<other_value_type, other_score_type> other;
  other.x1 = static_cast<other_value_type>(x1);
  other.y1 = static_cast<other_value_type>(y1);
  other.x2 = static_cast<other_value_type>(x2);
  other.y2 = static_cast<other_value_type>(y2);
  other.score = static_cast<other_score_type>(score);
  other.label_text = label_text;
  other.label = label;
  return other;
}

template <typename T1, typename T2>
template <typename O1, typename O2>
inline typename BoundingBoxType<T1, T2>::value_type
BoundingBoxType<T1, T2>::iou_of(const BoundingBoxType<O1, O2>& other) const {
  BoundingBoxType<value_type, score_type> tbox =
      other.template convert_type<value_type, score_type>();
  value_type inner_x1 = x1 > tbox.x1 ? x1 : tbox.x1;
  value_type inner_y1 = y1 > tbox.y1 ? y1 : tbox.y1;
  value_type inner_x2 = x2 < tbox.x2 ? x2 : tbox.x2;
  value_type inner_y2 = y2 < tbox.y2 ? y2 : tbox.y2;
  value_type inner_h = inner_y2 - inner_y1 + static_cast<value_type>(1.0f);
  value_type inner_w = inner_x2 - inner_x1 + static_cast<value_type>(1.0f);
  if (inner_h <= static_cast<value_type>(0.f) ||
      inner_w <= static_cast<value_type>(0.f))
    return std::numeric_limits<value_type>::min();
  value_type inner_area = inner_h * inner_w;
  return static_cast<value_type>(inner_area /
                                 (area() + tbox.area() - inner_area));
}

template <typename T1, typename T2>
inline cv::Rect BoundingBoxType<T1, T2>::rect() const {
  __assert_type<value_type, score_type>();
  auto boxi = this->template convert_type<int>();
  return cv::Rect(boxi.x1, boxi.y1, boxi.width(), boxi.height());
}

template <typename T1, typename T2>
inline cv::Point2i BoundingBoxType<T1, T2>::tl() const {
  __assert_type<value_type, score_type>();
  auto boxi = this->template convert_type<int>();
  return cv::Point2i(boxi.x1, boxi.y1 + 10);
}

template <typename T1, typename T2>
inline cv::Point2i BoundingBoxType<T1, T2>::bl() const {
  __assert_type<value_type, score_type>();
  auto boxi = this->template convert_type<int>();
  return cv::Point2i(boxi.x1, boxi.y2);
}

template <typename T1, typename T2>
inline cv::Point2i BoundingBoxType<T1, T2>::rb() const {
  __assert_type<value_type, score_type>();
  auto boxi = this->template convert_type<int>();
  return cv::Point2i(boxi.x2, boxi.y2);
}

template <typename T1, typename T2>
inline typename BoundingBoxType<T1, T2>::value_type
BoundingBoxType<T1, T2>::width() const {
  __assert_type<value_type, score_type>();
  return (x2 - x1 + static_cast<value_type>(1));
}

template <typename T1, typename T2>
inline typename BoundingBoxType<T1, T2>::value_type
BoundingBoxType<T1, T2>::height() const {
  __assert_type<value_type, score_type>();
  return (y2 - y1 + static_cast<value_type>(1));
}

template <typename T1, typename T2>
inline typename BoundingBoxType<T1, T2>::value_type
BoundingBoxType<T1, T2>::area() const {
  __assert_type<value_type, score_type>();
  return std::abs<value_type>(width() * height());
}

struct ObjectDetectionResult {
  std::vector<Boxi> result_bboxes;
  std::chrono::time_point<std::chrono::steady_clock> timestamp;
};

struct ObjectDetectionOption {
  std::string model_path;
  std::string label_path;
  int intra_threads_num = 2;
  int inter_threads_num = 2;
  float score_threshold = -1.f;
  float nms_threshold = -1.f;
  std::vector<int> class_name_whitelist;
  std::vector<int> class_name_blacklist;
  ObjectDetectionOption()
      : model_path(""),
        label_path(""),
        intra_threads_num(2),
        inter_threads_num(2) {}
  ObjectDetectionOption(const std::string mp, const std::string lp,
                        const int atm, const int etm, const float st,
                        const float nt, const std::vector<int>& cnw,
                        const std::vector<int>& cnb)
      : model_path(mp),
        label_path(lp),
        intra_threads_num(atm),
        inter_threads_num(etm),
        score_threshold(st),
        nms_threshold(nt),
        class_name_whitelist(cnw),
        class_name_blacklist(cnb) {}
};

#endif  // SUPPORT_INCLUDE_TASK_VISION_OBJECT_DETECTION_TYPES_H_
